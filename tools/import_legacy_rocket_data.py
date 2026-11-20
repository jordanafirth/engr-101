"""One-time export of the reviewed Engr 201 MATLAB/tunnel data to portable CSV.

Usage: pixi run python tools/import_legacy_rocket_data.py PATH_TO_ENGR_201
Requires authorized access to that source. Does not copy the old project.
"""

import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    legacy = args.source / "assignments" / "rocket_prediction"
    output = Path(__file__).resolve().parents[1] / "projects" / "rocket_prediction" / "data"
    output.mkdir(parents=True, exist_ok=True)
    mat_path = legacy / "EstesD12.mat"
    data = np.asarray(loadmat(mat_path)["EstesD12"], dtype=float)
    if data.shape[0] == 2:
        data = data.T
    if data.ndim != 2 or data.shape[1] != 2:
        raise ValueError("Expected EstesD12 time/thrust pairs.")
    added_origin = data[0, 0] > 0
    if added_origin:
        data = np.vstack(([0.0, 0.0], data))
    if (np.any(np.diff(data[:, 0]) <= 0) or np.any(data[:, 1] < 0)
            or data[0, 0] != 0 or data[0, 1] != 0 or data[-1, 1] != 0):
        raise ValueError("Unexpected D12 curve format.")
    np.savetxt(output / "estes_d12.csv", data, delimiter=",", fmt="%.12g",
               header="time_s,thrust_N", comments="")
    tunnel_path = legacy / "drag_data_2025.csv"
    rows = []
    with tunnel_path.open(encoding="utf-8", errors="replace", newline="") as handle:
        for row in csv.reader(handle):
            if len(row) != 4:
                continue
            try:
                values = [float(value) for value in row]
            except ValueError:
                continue
            if not np.all(np.isfinite(values)):
                raise ValueError("Nonfinite numeric tunnel record.")
            rows.append(values)
    if not rows:
        raise ValueError("No numeric tunnel rows found.")
    np.savetxt(output / "wind_tunnel_practice.csv", rows, delimiter=",", fmt="%.12g",
               header="pressure_kPa,temperature_C,speed_m_s,drag_N", comments="")
    metadata = {
        "source_repository": "https://github.com/usafa-engr-201/engr-201",
        "reviewed_local_revision": "b307a9e96fa7d3dbdfb82caf2f1197efcedc867d",
        "sources": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in [mat_path, tunnel_path]},
        "motor_variable": "EstesD12",
        "motor_label": "D12 (confirmed by course lead)",
        "prepended_zero_time_zero_thrust": bool(added_origin),
        "motor_rows": len(data), "tunnel_numeric_rows": len(rows),
        "transformations": ["Transpose MATLAB 2 by N array to time/thrust rows",
                            "Prepend (0 s, 0 N) when missing",
                            "Normalize tunnel column labels; omit headers, units, and trailing metadata",
                            "Retain numeric values to 12 significant digits"],
    }
    (output / "provenance.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(data)} D12 points and {len(rows)} practice tunnel rows.")


if __name__ == "__main__":
    main()
