# Rocket Prediction Validation

## Executed checks

The worked notebook executed in a fresh Jupyter kernel on Windows using a project-local validation runtime with Python 3.12.14 and NumPy 2.5.5. All code cells completed, including plots, convergence and sensitivity studies, and prediction export. The trajectory figure was visually inspected for readable labels, distinct event markers, correct units, and the demonstration-input label.

Seven automated checks passed:

1. Notebook schemas, code syntax, five explicit student exercise stops, and unescaped mathematical notation.
2. Drag direction in ascent and descent, zero-speed drag, and a known net-force calculation.
3. Free-fall velocity against the analytic solution and the expected reduction in first-order height error.
4. D12 curve identity, 1.650 s burnout, and impulse between 16 and 18 N·s.
5. Increasing time, nonnegative height, touchdown, event-aligned burnout/deployment, and apogee convergence.
6. Physical sensitivity to mass, body Cd, and air density.
7. Invalid inputs, no liftoff, and an explicit stop if touchdown is not reached within the allotted simulation time.

The worked notebook produced motor, Cd, and trajectory figures. At dt = 0.020 s, the **demonstration configuration** predicted about 58.286 m peak height, 4.210 s to peak, 25.926 m/s maximum upward velocity, and 18.892 s to touchdown. The apogee change between dt = 0.010 and 0.005 s was approximately 0.0056 m. These are reproducibility checks for the example, not predictions for measured flight hardware.

The student notebook is deliberately incomplete. Its exercise cells raise named `NotImplementedError` messages until completed; it is not expected to run to the end unchanged. The worked companion completes the same code exercises and provides the end-to-end execution check.

## Environment status

The Pixi 0.84.2 solver generated a lockfile for Windows x64, Linux x64, Intel macOS, and Apple silicon. Initial conda package installation failed at the package host with DNS resolution errors. A retry stalled and was stopped. The final manifest uses matplotlib-base to avoid unnecessary desktop Qt dependencies. Notebook execution was verified separately using dependencies installed into the ignored local tools directory. That runtime is not a replacement for the student installation instructions and is not committed.

The full locked Pixi install and classroom launch must still be confirmed on a cadet laptop. Linux and macOS lock resolution has not been supplemented by execution on those systems. Keep the lockfile stable once the class deployment is verified, and review dependency updates deliberately.

## Remaining instructional review

Confirm actual vehicle and tunnel reference dimensions, total representative mass, environmental inputs, recovery configuration, and the tested motor variant's delay. Replace practice tunnel data with the field-trip measurements before making a real preflight prediction. Review the amount of supplied bookkeeping and exercise difficulty with the other instructor. This is a reviewed draft project, not a demonstrated classroom delivery.
