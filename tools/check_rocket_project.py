"""Validate both notebooks and execute the worked example in a temporary kernel.

Run from the repository root with `pixi run check`.
"""

from dataclasses import replace
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects" / "rocket_prediction"
sys.path.insert(0, str(PROJECT))
from flight_support import FlightInputs, load_motor, simulate, summary

WORKED = nbformat.read(PROJECT / "rocket_prediction_worked.ipynb", as_version=4)
SCOPE = {}
for cell in WORKED.cells:
    if cell.metadata.get("exercise") in {"drag", "acceleration", "step"}:
        exec(cell.source, SCOPE)
DRAG, STEP = SCOPE["drag_force"], SCOPE["advance_step"]
MOTOR_T, MOTOR_F = load_motor(PROJECT / "data" / "estes_d12.csv")
BASE = FlightInputs(0.40, 0.95, 0.4, np.pi * 0.0574**2 / 4,
                    1.75, np.pi * 0.6096**2 / 4, 3.0)


class FlightChecks(unittest.TestCase):
    def test_notebook_structure_and_starter_stops(self):
        student = nbformat.read(PROJECT / "rocket_prediction.ipynb", as_version=4)
        for notebook in [student, WORKED]:
            nbformat.validate(notebook)
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    compile(cell.source, "notebook-cell", "exec")
            self.assertTrue(all("\\\\frac" not in cell.source for cell in notebook.cells))
        exercises = [cell for cell in student.cells if "student-exercise" in cell.metadata.get("tags", [])]
        self.assertEqual(len(exercises), 5)
        for cell in exercises:
            self.assertIn("NotImplementedError", cell.source)
        first = next(cell for cell in exercises if cell.metadata.exercise == "estimate")
        with self.assertRaisesRegex(NotImplementedError, "Exercise 1"):
            exec(first.source, {})

    def test_drag_and_known_force_case(self):
        self.assertAlmostEqual(DRAG(1, 10, 0.5, 0.01), -0.25)
        self.assertAlmostEqual(DRAG(1, -10, 0.5, 0.01), 0.25)
        self.assertEqual(DRAG(1, 0, 0.5, 0.01), 0)
        self.assertAlmostEqual(SCOPE["acceleration"](8, -1, 0.5, 9.8), 4.2)

    def test_freefall_against_analytic_solution(self):
        errors = []
        for dt in [0.1, 0.05, 0.025]:
            h, v = 100.0, 5.0
            for _ in range(round(1 / dt)):
                h, v, a = STEP(h, v, 0, 0, 0.5, 9.81, dt)
            self.assertAlmostEqual(v, 5 - 9.81)
            errors.append(abs(h - (100 + 5 - 0.5 * 9.81)))
        self.assertAlmostEqual(errors[1] / errors[0], 0.5)
        self.assertAlmostEqual(errors[2] / errors[1], 0.5)

    def test_motor_impulse_and_source(self):
        # The reviewed D12 curve is about 16.8 N·s, not the incomplete E12 starter.
        self.assertTrue(16 < np.trapezoid(MOTOR_F, MOTOR_T) < 18)
        self.assertAlmostEqual(MOTOR_T[-1], 1.65)
        provenance = json.loads((PROJECT / "data" / "provenance.json").read_text())
        self.assertEqual(provenance["motor_variable"], "EstesD12")
        self.assertTrue(provenance["prepended_zero_time_zero_thrust"])

    def test_flight_events_and_convergence(self):
        heights = []
        for dt in [0.04, 0.02, 0.01, 0.005]:
            flight = simulate(BASE, MOTOR_T, MOTOR_F, DRAG, STEP, dt_s=dt)
            self.assertTrue(np.all(np.diff(flight["time_s"]) > 0))
            self.assertTrue(np.all(flight["altitude_m"] >= 0))
            self.assertEqual(flight["altitude_m"][-1], 0)
            self.assertLess(flight["velocity_m_s"][-1], 0)
            self.assertTrue(np.any(np.isclose(flight["time_s"], MOTOR_T[-1])))
            self.assertTrue(np.any(np.isclose(flight["time_s"], flight["deployment_s"])))
            self.assertIn("parachute", flight["phase"])
            heights.append(summary(flight)["apogee_m"])
        self.assertLess(abs(heights[-1] - heights[-2]), 0.5)
        self.assertLess(abs(heights[-1] - heights[-2]), abs(heights[1] - heights[0]))

    def test_physical_sensitivity(self):
        def peak(inputs):
            return summary(simulate(inputs, MOTOR_T, MOTOR_F, DRAG, STEP, dt_s=0.005))["apogee_m"]
        base_peak = peak(BASE)
        self.assertLess(peak(replace(BASE, body_cd=0.8)), base_peak)
        self.assertGreater(peak(replace(BASE, density_kg_m3=0.8)), base_peak)
        self.assertLess(peak(replace(BASE, mass_kg=0.44)), base_peak)

    def test_invalid_input_no_liftoff_and_timeout(self):
        for invalid in [replace(BASE, mass_kg=0), replace(BASE, body_cd=-1)]:
            with self.assertRaises(ValueError):
                simulate(invalid, MOTOR_T, MOTOR_F, DRAG, STEP)
        with self.assertRaisesRegex(RuntimeError, "No liftoff"):
            simulate(replace(BASE, mass_kg=10), MOTOR_T, MOTOR_F, DRAG, STEP)
        with self.assertRaisesRegex(RuntimeError, "No touchdown"):
            simulate(BASE, MOTOR_T, MOTOR_F, DRAG, STEP, max_time_s=0.5)
        with self.assertRaises(ValueError):
            simulate(BASE, MOTOR_T, MOTOR_F, DRAG, STEP, dt_s=0)


def execute_worked_notebook():
    output = ROOT / "build" / "rocket_prediction"
    output.mkdir(parents=True, exist_ok=True)
    for variable, folder in [("IPYTHONDIR", "ipython"), ("JUPYTER_RUNTIME_DIR", "jupyter"),
                             ("MPLCONFIGDIR", "matplotlib")]:
        path = output / folder
        path.mkdir(exist_ok=True)
        os.environ[variable] = str(path)
    with tempfile.TemporaryDirectory(prefix="engr101-kernel-") as temporary:
        kernel_dir = Path(temporary) / "engr101-check"
        kernel_dir.mkdir()
        (kernel_dir / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Engr 101 validation", "language": "python",
        }), encoding="utf-8")
        specs = KernelSpecManager(kernel_dirs=[temporary])
        manager = KernelManager(kernel_name="engr101-check", kernel_spec_manager=specs)
        notebook = nbformat.read(PROJECT / "rocket_prediction_worked.ipynb", as_version=4)
        client = NotebookClient(notebook, km=manager, timeout=120,
                                resources={"metadata": {"path": str(PROJECT)}})
        executed = client.execute()
        nbformat.write(executed, output / "rocket_prediction_worked_executed.ipynb")
    images = sum(1 for cell in executed.cells if cell.cell_type == "code"
                 for item in cell.get("outputs", []) if "image/png" in item.get("data", {}))
    if images < 3:
        raise AssertionError(f"Expected motor, Cd, and trajectory plots; found {images}.")
    print(f"Executed worked notebook in a fresh kernel; {images} plots. Output: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FlightChecks))
    if not result.wasSuccessful():
        raise SystemExit(1)
    execute_worked_notebook()
