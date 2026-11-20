# Rocket Prediction Data Provenance

The project bundles two small, transformed datasets so the notebook does not depend on a local `D:` drive, a MATLAB installation, or a private-repository download during class.

## D12 thrust

`estes_d12.csv` is exported from the `EstesD12` variable in Engr 201's `assignments/rocket_prediction/EstesD12.mat`. The reviewed local revision was `b307a9e96fa7d3dbdfb82caf2f1197efcedc867d` of [the private course repository](https://github.com/usafa-engr-201/engr-201).

The source stores a 2 by 20 matrix of time in seconds and thrust in newtons. The export transposes it to rows and prepends a (0 s, 0 N) point because the source begins at 0.049 s. Burnout is 1.650 s; the source already ends at zero thrust. The 21-point exported curve has a trapezoidal impulse of 16.8391395 N·s. These values identify the supplied teaching curve; they are not a certification of an individual motor.

The course lead explicitly confirmed D12. Do not reuse the incomplete E12-labeled matrix in the old MATLAB starter. Recovery delay is a separate configuration input, not encoded in the thrust CSV; confirm the actual D12 variant before a flight prediction.

## Practice wind-tunnel measurements

`wind_tunnel_practice.csv` contains all eight numeric measurement rows from `assignments/rocket_prediction/drag_data_2025.csv`. The original labels identify pressure in kPa, temperature in °C, velocity in m/s, and force in N. Its trailing text identifies 3 September 2025 and an Engr 495 rocket. Header, units, blank rows, and trailing metadata were normalized into this description; no numeric measurement rows were selected out.

The notebook uses a declared example reference diameter to practice calculating Cd. The legacy CSV does not establish the tested model's reference dimensions. The resulting practice Cd is not a verified coefficient for the Engr 101 rocket. Replace the CSV and reference area using actual field-trip measurements and instructor-approved data handling. Preserve raw measurements separately.

## Reproducing the export

`provenance.json` records source SHA-256 hashes and transformations. With an authorized local checkout of Engr 201:

```sh
pixi run python tools/import_legacy_rocket_data.py PATH_TO_ENGR_201
```

Run from the Engr 101 repository root. This overwrites the two teaching CSVs and provenance file, so use it deliberately when updating the reference data. NumPy and SciPy support this instructor conversion; students read the normalized CSVs directly with NumPy and do not need MATLAB or a separate file conversion step.
