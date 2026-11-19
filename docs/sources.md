# Engr 101 Reference Sources

## Private Engr 201 repository

- Remote: [usafa-engr-201/engr-201](https://github.com/usafa-engr-201/engr-201).
- Local source revision reviewed: `b307a9e96fa7d3dbdfb82caf2f1197efcedc867d`.
- Original local location: `D:\dfas\engr-201`; this path is machine-specific and is not required on a new computer.
- The local copy had unrelated changes under ASTRO and generated atmosphere files. Those files were not used to define Engr 101 and were not copied here.

The remote is private. GitHub account authorization and machine authentication are separate requirements: the account must have repository read permission, and Git on the new computer must sign in as that account. Organization single sign-on may require an additional authorization if the organization enforces it. Do not make the repository public or put tokens in these files.

An authenticated checkout can be obtained separately:

```sh
git clone https://github.com/usafa-engr-201/engr-201.git
```

Keep it outside this repository unless deliberately establishing a submodule later. Repository links require the reader to sign in to an authorized GitHub account; they do not grant access themselves. A prior unauthenticated API request returned 404, which did not establish that the repository was missing. Prefer the existing authenticated Git workflow when available.

The course map links to files at the reviewed commit so the reference version does not drift. A new development session can inspect newer upstream material if needed and record the revision used.

An authenticated `git ls-remote` check succeeded on the original computer during handoff preparation. The remote HEAD was `5532a4d1c7ba6e9d338ada2d301434710ca7691a`, newer than the reviewed local revision. No GitHub access change was needed on that computer; the newer remote contents have not yet been reviewed. Check access on another computer with `git ls-remote https://github.com/usafa-engr-201/engr-201.git HEAD` after authenticating.

## Reviewed material

| Source path within Engr 201 | Relevance |
| --- | --- |
| `SYLLABUS.MD` | Existing sequence, communication, and technical skills; old policies are not Engr 101 policy |
| `notes/06 modeling.md` | Modeling examples; rewrite for freshman preparation and check equations |
| `notes/07 numerical integration.md` | Numerical flight approach; check notation and remove advanced prerequisite assumptions |
| `assignments/rocket_prediction/ASSIGNMENT_INSTRUCTIONS.md` | Prediction progression; remove Simulink and replace fitted Cd with the straight mean |
| `assignments/rocket_prediction/rocket_prediction_algorithm.md` | Starting algorithm; reconcile update conventions before Python implementation |
| `assignments/rocket_instrumentation/ASSIGNMENT_INSTRUCTIONS.md` | Acquisition, altitude characterization, and flight-event logic |
| `assignments/rocket_instrumentation/src/` and `platformio.ini` | Existing embedded implementation and dependencies; not yet built or validated for Engr 101 |
| `assignments/arduino_intro/ASSIGNMENT_INSTRUCTIONS.md` | Upload, simple modifications, and nonblocking timing exercises |
| `assignments/rocket_launch/ASSIGNMENT_INSTRUCTIONS.md` | Readiness and quick-look communication; procedure authorship probably omitted |
| `assignments/rocket_launch/test_readiness_report.md` | Existing readiness structure; operating limits require current local review |
| `assignments/paper/ASSIGNMENT_INSTRUCTIONS.md` | Cumulative writing and peer review; simplify for a likely group report |

One concrete correction identified during review: the numerical-integration notes label the integral of force over time as a height change, although the prose identifies impulse correctly. Reuse needs technical review, not just translation from MATLAB.

## Blackboard documentation

These official references informed the planning proposal; they do not identify the Academy's installed version or verify its configuration:

- [Question types](https://help.anthology.com/blackboard/instructor/en/assessments/questions/question-types.html).
- [Question banks](https://help.anthology.com/blackboard/instructor/en/assessments/questions/reuse-questions/question-banks.html).

## Information still to obtain

The established sprint materials, final provost policy, actual section calendars, and Blackboard course details have not been supplied. They should be obtained from the lead or the applicable institutional system rather than inferred from old course documents.
