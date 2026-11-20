# D12 Rocket Prediction Project

A guided Jupyter adaptation of the Engr 201 MATLAB rocket-prediction project for freshmen in Engr 101. Students build the force balance and numerical update, use a straight-average measured Cd, and explain what makes their prediction credible.

## Open the project

Install [Pixi](https://pixi.prefix.dev/latest/installation/) once using the appropriate installer for your computer. From the repository root:

```sh
pixi install --locked
pixi run lab
```

Open `rocket_prediction.ipynb` with the Python 3 kernel. The manifest and lockfile specify the environment; do not install packages inside notebook cells. First setup requires network access. The local notebook and bundled data need no network once dependencies are installed.

Work on a copy of the student notebook. Run cells in order with Shift+Enter. Five exercise cells deliberately raise `NotImplementedError` until completed. Later cells depend on those answers. Restart the kernel and run all cells before submission. A short assertion message identifies common mistakes in signs, force balance, or updates.

Pixi resolves environments for Windows x64, Linux x64, Apple silicon, and Intel macOS. Only the available Windows machine is used for execution checks; resolution does not establish classroom deployment on every platform. See [validation status](#validation-status).

## Files

| File | Purpose |
| --- | --- |
| [rocket_prediction.ipynb](rocket_prediction.ipynb) | Student project with explanations, five code exercises, checks, plots, and written-response prompts |
| [rocket_prediction_worked.ipynb](rocket_prediction_worked.ipynb) | Completed code for instructor review or later release as an open teaching example; written interpretation remains for students |
| [flight_support.py](flight_support.py) | Provided flight-loop and event bookkeeping; student physics functions are passed into it |
| [data](data/README.md) | Portable D12 thrust and legacy practice wind-tunnel data, with provenance |
| `outputs/` | Ignored local figures and timestamped prediction exports |

The worked notebook is not a secure exam key. Distribute only the student notebook and support/data files if students should complete the code before seeing the worked version.

## Learning sequence

1. Identify a configuration, sources, coordinate reference, and assumptions.
2. Inspect D12 thrust and estimate burnout speed and peak height using impulse.
3. Calculate individual tunnel Cd values and their straight arithmetic average.
4. Implement drag that opposes velocity and acceleration from the signed force sum.
5. Implement a first-order semi-implicit Euler time step.
6. Predict powered flight, coast, fixed-delay parachute recovery, and touchdown.
7. Check time-step convergence and physical-input sensitivity.
8. Preserve a timestamped prediction and write a concise engineering argument.

Use sections 1–2 with initial modeling lessons, sections 3–5 around the wind-tunnel and numerical-method lessons, and sections 6–9 for the prediction checkpoint. Instructor pacing should follow actual student preparation rather than assigning the entire notebook at once. The net-force lesson and hand calculations must precede the corresponding code exercise.

## Configuration and scope

The motor is **D12**, as confirmed by the course lead. Example mass, body diameter, air density, parachute diameter/Cd, and recovery delay are explicitly demonstration assumptions. The course's approximately 600 mm length is context, not a substitute for measured mass or frontal area. The desired maximum altitude is 100 m; the notebook compares its prediction with that target but does not establish launch authorization or a validated operating limit.

The model is vertical in still air, with constant mass, gravity, and density. It uses piecewise-linear thrust, signed quadratic drag, and instantaneous fixed-delay recovery deployment. It does not model lateral flight, launch stability, parachute-opening loads, changing mass, or the later altitude-triggered Rocket 2 mechanism. The provided loop handles pad support and interpolated touchdown; students supply the drag and motion equations.

The update uses the new velocity for height: semi-implicit Euler. This is made explicit rather than mixing it with the old-velocity explicit Euler formula. Event-aligned steps split at thrust samples and recovery deployment. The notebook checks apogee changes under smaller time steps and distinguishes that numerical error from uncertainty in physical inputs.

The practice tunnel data do not characterize the new rocket. Replace them and the reference area with measurements from the downstairs field trip before recording a real flight prediction. Use the straight mean; no curve fitting, atmosphere-calculator assignment, or Simulink is included.

## Instructor review and validation

```sh
pixi run check
```

This validates notebook structure, checks drag signs and known force cases, compares free fall with an analytic solution, checks D12 impulse, event timing, convergence, input validation and no-liftoff behavior, and executes the worked notebook in a new Jupyter kernel. An executed review copy is written under the ignored `build/rocket_prediction/` directory. The incomplete student notebook is checked for clear exercise stops rather than incorrectly treated as a finished program.

The editable notebook source is [the build script](../../tools/build_rocket_notebooks.py). Modify that script and regenerate both notebooks with:

```sh
pixi run python tools/build_rocket_notebooks.py
```

Do not regenerate over a student's completed notebook. Neither generation nor validation alters a student's personal copy.

### Validation status

The cross-platform Pixi lockfile was generated with Pixi 0.84.2. Initial environment installation encountered a DNS failure at the conda package host. A separate ignored project-local validation runtime was prepared to check the notebooks independently. Execution results and any remaining installation limitation are recorded in [the project validation note](validation.md). Test the actual Pixi installation and notebook launch on a cadet laptop before classroom deployment.

## Original sources

Adapted from the private [Engr 201 rocket-prediction assignment](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/rocket_prediction/ASSIGNMENT_INSTRUCTIONS.md) and algorithm at the same reviewed revision. The legacy starter contains an E12 label and incomplete example; this project uses `EstesD12.mat` instead. See [data provenance](data/README.md) and the repository [source guide](../../docs/sources.md). No full source-repository snapshot is included.
