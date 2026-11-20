# Engr 101 Course Design Draft

Engr 101 introduces engineering through a four-lesson design sprint followed by a semester-long rocket project. Students learn to frame a problem, develop and check a model, build and test a system, and communicate conclusions supported by evidence. The rocket provides a shared setting for mechanics, computation, electronics, mechanical design, and engineering judgment.

The course serves freshmen in every major and establishes practices that the remaining four courses can develop with greater technical depth and student independence.

## Planning basis

### Established decisions

- Four credit hours; 41 lessons of two continuous hours on an alternating A-day/B-day schedule, giving 82 scheduled contact hours.
- Almost all students concurrently take Calc II. Science 1 provides some concurrent physics, but its detailed alignment is not yet established.
- Lessons 1–4 are an unrelated, hands-on design sprint. Lesson 5 introduces engineering by examining the sprint and connecting it to the rocket mission.
- The rocket project includes an F=ma flight model in a Jupyter notebook, an Arduino instrumentation package, ground testing, a first launch, comparison of predictions with measurements, a student-designed altitude-triggered deployment mechanism, a second launch, and analysis.
- Retain the downstairs wind-tunnel field trip around lesson 10. Students collect drag data and use a straight average of calculated drag coefficients.
- Remove the atmosphere calculator and Simulink entirely.
- Procedures probably will not be a separate assignment. The technical paper will be easier than Engr 201 and probably completed by groups.
- Teamwork, communication, ethics, models, and related engineering topics recur throughout the semester.
- The experimental course starts 6 January 2027 with two instructors and two sections of 20 students each. Rocket 1 equipment is available.
- The existing sprint has been tested for many semesters in another class and will be run by an instructor familiar with it. Adopt that sprint rather than developing a replacement.
- Plan to introduce every necessary technical component. Familiarity with force can be assumed; summing forces must be introduced. Do not depend on Science 1 coordination before the semester.
- Rocket baseline: approximately 600 mm long, D12 motor, desired maximum altitude 100 m because of airspace and field size. Motor choice may need reconsideration as mass changes; changes require a new prediction and review against operating constraints.
- A high proportion of the grade must be earned independently in class; 80% remains the conservative planning assumption, but the final percentage is unsettled. Use paper, pencil, and calculator for this work: no AI, group work, phones, internet, or computers. Reference-sheet rules remain to be set.
- Students must complete a preflight homework before every class. Plan online, automatically graded preparation in Blackboard, with the exact course version and configuration to be confirmed.
- Schedule three term tests, with Test 3 around lesson 35 or earlier, plus a separate final examination.
- Rocket 2 requires substantial development after the semester begins. Engr 202 development is deferred until late spring or summer; the Engr 101 lead also leads Engr 202.

### Proposed choices for this draft

- Assume no prior programming. Provide starter notebooks, hardware support, and short programming exercises tied to immediate project needs.
- Use five teams of four per section, giving ten teams total. Confirm this arrangement against available equipment; rotate responsibilities and assess individual understanding.
- Use a simpler group paper, developed through revisions, plus a short final team briefing. These are planning assumptions pending the final communication requirement.
- Target first launch at lesson 20 and second launch at lesson 36. Reserve lessons 21 and 37 for launch contingency or follow-up testing.
- Schedule Tests 1, 2, and 3 in lessons 14, 23, and 33. Schedule the final separately in the official exam period, date to be confirmed. Use lesson 41 for synthesis, closure, and final preparation.
- Use the deployment mechanism to demonstrate a benign physical action whose completion can be observed. Define the specific payload, mechanism boundaries, flight conditions, and integration constraints before writing the assignment.
- Provide atmospheric properties and supported conversion routines. Students explain what those inputs mean and check units without implementing an atmosphere calculator.
- Use Pixi to define and lock the Python/Jupyter environment. The [guided D12 project](projects/rocket_prediction/README.md) is the initial notebook implementation; review its demonstration inputs and classroom setup before use.

Existing Engr 201 student policies and assignment instructions are reference material. They do not automatically establish Engr 101 policies, grading rules, or software requirements.

## Course outcomes

By the end of the course, each student should be able to:

| Outcome | Capability | Evidence |
| --- | --- | --- |
| O1 | Translate a need into measurable requirements and identify constraints and tradeoffs | Sprint criteria; deployment requirements and concept comparison |
| O2 | Construct and check a one-dimensional force-based numerical model and explain its assumptions and limitations | Flight notebook; individual model explanation |
| O3 | Acquire and interpret sensor data, establish a reference, and characterize measurement variability and error | Instrument tests; flight data analysis |
| O4 | Develop and integrate mechanical components, electronics, and software | Instrument package; functioning deployment prototype |
| O5 | Plan tests, compare results with predictions or requirements, and use discrepancies to guide improvement | Ground tests; both flight assessments |
| O6 | Work responsibly in a team and communicate decisions and conclusions with traceable evidence | Team practices; report revisions; briefing; individual explanations |

## Lesson map

The evidence column describes what students produce or demonstrate. Most entries are brief work products, notebook cells, or instructor observations rather than separately graded submissions. Outcome codes identify the principal emphasis of each lesson.

### Lessons 1 through 5

| Lesson | Question and activity | Student evidence | Engineering emphasis | Outcomes |
| --- | --- | --- | --- | --- |
| 1 | What would count as a successful solution? Introduce the sprint, inspect materials, form teams, and build and test an initial concept | Initial concept, prediction, and first test result | Needs, constraints, participation, honest recording | O1, O5, O6 |
| 2 | What alternatives are worth trying? Sketch alternatives, make simple predictions, and choose a revised concept | Concept comparison and reason for selection | Models, tradeoffs, team decisions | O1, O2, O6 |
| 3 | What does testing tell us to change? Conduct repeated tests, diagnose weaknesses, and revise | Comparable test results and documented change | Variability, iteration, fair comparisons | O4, O5 |
| 4 | What can we demonstrate and defend? Complete a common performance test and short team briefing | Demonstration and concise explanation of evidence and limitations | Communication, ethical reporting, team reflection | O5, O6 |
| 5 | What did we just do as engineers? Build an engineering framework from sprint experiences; introduce the rocket mission and sequence | Sprint-to-rocket comparison and initial questions about the mission | Engineering overview, uncertainty, responsibility, disciplinary connections | O1, O6 |

### Lessons 6 through 12

| Lesson | Question and activity | Student evidence | Engineering emphasis | Outcomes |
| --- | --- | --- | --- | --- |
| 6 | How can a notebook support an engineering argument? Run and modify a starter notebook; work with variables, units, tables, and plots | Executable notebook with a simple calculation and labeled plot | Reproducibility, units, basic computation | O2, O6 |
| 7 | What determines rocket motion? Introduce net force as the signed sum of forces, draw force diagrams, and use the net force in F=ma | Force balance and checked calculations for several flight conditions | Net force, mechanics, assumptions, sign conventions | O2 |
| 8 | How can small steps predict a trajectory? Calculate motion by hand for a few steps, then implement a scaffolded loop | Simple numerical trajectory and comparison with a known case | Rates, accumulation, checking code against physics | O2 |
| 9 | What do we need from the wind tunnel? Introduce drag, calculate Cd from sample data, and prepare a shared data sheet | Predicted trends, units, and completed practice calculation | Measurement planning, references, division of work | O2, O3, O6 |
| 10 | How much drag does our rocket produce? Visit the downstairs wind tunnel and collect force and speed data with the relevant conditions | Recorded data and observations about the setup | Experimental practice, physical models and their limits | O3, O5 |
| 11 | What Cd will we use? Calculate Cd for the designated valid measurements, take a straight arithmetic average, and plot the individual values | Mean Cd, data plot, and explanation of variation | Transparent data handling, uncertainty, concise figures | O2, O3, O6 |
| 12 | How credible is our flight prediction? Integrate supplied thrust data, measured mean Cd, gravity, and defined flight phases; check time-step sensitivity | Draft flight prediction and checks | Model verification, empirical inputs, assumptions | O2, O5 |

### Lessons 13 through 22

| Lesson | Question and activity | Student evidence | Engineering emphasis | Outcomes |
| --- | --- | --- | --- | --- |
| 13 | How do we turn a prediction into a useful claim? Complete model checks, vary an important input, and review prediction figures and text | Paper checkpoint 1 and runnable notebook | Sensitivity, limitations, technical communication | O2, O6 |
| 14 | Test 1: individually apply engineering fundamentals and flight modeling from lessons 1–13 | Individual test responses | Requirements, force balance, numerical steps, Cd, model checks, interpretation | O1, O2, O3, O5, O6 |
| 15 | How does a sensor become a useful measurement? Trace power, sensor, controller, and storage; upload supported firmware, establish an altitude reference, and collect initial readings | Working acquisition and explanation of the signal path and reference | Circuits, embedded computation, pressure-derived altitude | O3, O4 |
| 16 | Can we trust the recorded data? Compare known elevation changes, repeat measurements, and test battery operation, timestamps, sampling, storage, and restart behavior | Instrument characterization and end-to-end test record | Bias, repeatability, reliability, traceable configuration | O3, O4, O5 |
| 17 | How do we recognize events? Develop simple flight-state or event logic and test it using supplied or recorded data | Event table, test cases, and observed transitions | Algorithms, thresholds, false triggers, software testing | O4, O5 |
| 18 | What changes when the instrument is installed? Assemble and mount the package, measure the flight configuration, and repeat integrated checks | Measured configuration and integrated test results | Mechanical interfaces, mass, packaging, teamwork | O4, O5, O6 |
| 19 | What evidence makes us ready to launch? Present a short readiness argument, inspect the configuration, and freeze the preflight prediction | Paper checkpoint 2 and concise readiness record | Evidence-based decisions, responsibilities, risk | O2, O5, O6 |
| 20 | What happens in flight? Conduct first launch and record actual configuration, conditions, and observations | Flight data, configuration record, and quick-look summary | Test execution, roles, accurate reporting | O3, O5, O6 |
| 21 | What evidence is missing? Reserve for postponed launch, recovery of data, instrument diagnosis, or repeat ground tests | Recovered data or targeted follow-up evidence | Contingency, diagnosis, disciplined iteration | O3, O5 |
| 22 | How did prediction compare with flight? Align time and altitude references, compare trajectories and key quantities, and investigate discrepancies | Comparison figures, quantitative differences, and supported explanations | Validation, measurement limits, competing explanations | O2, O3, O5 |

### Lessons 23 through 32

| Lesson | Question and activity | Student evidence | Engineering emphasis | Outcomes |
| --- | --- | --- | --- | --- |
| 23 | Test 2: individually interpret instrumentation and first-flight evidence from lessons 15–22, with essential modeling revisited | Individual test responses; paper checkpoint 3 is submitted separately before this meeting | Measurement, flight comparisons, evidence, ethical reporting | O2, O3, O4, O5, O6 |
| 24 | What must deployment accomplish, and what solutions could work? Define measurable requirements, generate alternative concepts, and sketch their interfaces | Requirement-to-test table and distinct concepts | Requirements, flight direction, references, tolerances, creativity, interfaces | O1, O4, O5 |
| 25 | Which concept should we develop? Compare alternatives using relevant criteria and evidence; identify the most useful early test | Concept selection and planned test of a critical uncertainty | Tradeoffs, uncertainty, responsible team decisions | O1, O5, O6 |
| 26 | How can we test the mechanism idea quickly? Build a low-cost physical prototype and test the difficult part first | Prototype result and design revision | Prototyping, fabrication, learning before committing | O4, O5 |
| 27 | What physical details determine performance? Develop mounting, geometry, loads, fits, and an appropriate drawing or CAD model | Buildable design with critical dimensions and interfaces | Mechanical reasoning, manufacturability | O2, O4 |
| 28 | Can the electronics drive the mechanism? Use a supported actuator circuit and test power, command, and physical response | Measured command-to-action behavior | Electrical power, actuation, integration | O3, O4, O5 |
| 29 | When should the system act? Implement altitude and flight-state conditions; test crossings, noise, repeat triggering, and reset behavior | Trigger logic and test results using replayed or synthetic data | State, algorithms, edge cases | O1, O4, O5 |
| 30 | Does the design form a coherent system? Review requirements, physical design, interfaces, software, and test evidence before completing flight hardware | Paper checkpoint 4 and updated verification table | Design review, evidence gaps, communication | O1, O4, O5, O6 |
| 31 | Does the complete system work? Build and integrate the mechanism, instrument, actuator, and software | Integrated prototype and recorded issues | System integration, configuration, troubleshooting | O4, O5 |
| 32 | Does it work repeatedly under relevant conditions? Repeat integrated tests and measure physical completion, timing, and variability | Requirement-by-requirement ground-test results | Verification, repeatability, limitations | O3, O5 |

### Lessons 33 through 41

| Lesson | Question and activity | Student evidence | Engineering emphasis | Outcomes |
| --- | --- | --- | --- | --- |
| 33 | Test 3: individually evaluate deployment requirements, concepts, integration, and verification from lessons 24–32, with earlier fundamentals revisited | Individual test responses | Requirements, tradeoffs, mechanism and actuator reasoning, event logic, test adequacy | O1–O6 |
| 34 | What must change before flight, and what will the flight establish? Correct priority issues and repeat affected checks; update the supported flight notebook for the actual configuration and plan observations | Corrective-action evidence, frozen second-flight prediction, and evidence plan | Iteration, coupled effects, prediction, test adequacy | O1, O2, O4, O5 |
| 35 | Is the complete system ready? Demonstrate the ground sequence and review requirements, unresolved limitations, and flight configuration | Second readiness record and configuration identification | Technical responsibility, candid decisions, team coordination | O4, O5, O6 |
| 36 | Does the design perform in flight? Conduct the second launch and observe both command and physical deployment | Flight data, physical-action evidence, and quick-look summary | Integrated performance, observation, reporting | O3, O4, O5, O6 |
| 37 | What follow-up evidence do we need? Reserve for delayed flight, data recovery, diagnosis, or targeted repeat tests | Additional evidence addressing a specific gap | Contingency, test selection, uncertainty | O3, O5 |
| 38 | Which requirements did we meet? Compare predictions, commands, and observed action; distinguish success, failure, and insufficient evidence | Completed performance table and analysis figures | Validation, ethics, qualified conclusions | O1, O3, O5, O6 |
| 39 | What can we conclude, and what transfers? Peer-review the final argument and solve a short individual problem in a different engineering context | Final paper revision and individual transfer exercise | Communication, generalization, limits of claims | O1, O2, O5, O6 |
| 40 | Can we explain and defend our work? Deliver team briefings with questions directed to different members | Team briefing and individual responses | Audience, evidence, technical judgment | O6 |
| 41 | What carries beyond this project? Synthesize the course, practice transfer to another system, and prepare for the separate final examination | Individual practice argument and course reflection | Transfer, accountability, synthesis | O1–O6 |

The final examination is additional to the 41 lessons and occurs in the official exam period; its date and duration remain to be confirmed. Test 3 remains at lesson 33, before the second launch and within the required placement of approximately lesson 35 or earlier.

## Opening design sprint

Adopt the existing, repeatedly taught sprint and its established materials, test arrangements, and instructor practices. The lesson 1–4 entries describe intended engineering experiences, not a requirement to change the trusted sprint's internal sequence. Obtain its handout and schedule, then reconcile the course map with what students actually do.

Capture enough of the experience to support lesson 5: how teams interpreted success, considered alternatives, tested a solution, and responded to results. Use existing sprint artifacts wherever possible. Avoid adding a substantial sprint paper or redesigning the activity during the startup period.

Lesson 5 should give names to experiences students have already had: requirements, constraints, models, tradeoffs, iteration, verification, uncertainty, and professional responsibility. A short working definition of engineering is sufficient. Use brief reflection questions later to examine rules of thumb and their limits rather than teaching an opening survey of engineering philosophy.

## Recurring engineering topics

| Topic | Introduce | Apply and revisit | Evidence within existing work |
| --- | --- | --- | --- |
| Teamwork | Sprint roles, participation, and decision making | Establish rocket team agreements after lesson 5; review after first flight and before final reporting | Role rotation, brief contribution records, two team reflections |
| Communication | Sketches and a short sprint briefing | Notebook explanations, tunnel data, prediction figures, readiness discussions, final paper and briefing | A claim supported by a figure or table; revisions after feedback |
| Ethics | Consistent test rules and honest sprint results | Preserve original data; document assistance; disclose instrument problems; report unmet requirements | Traceable data, acknowledgment, candid limitations and conclusions |
| Models | Simple sprint prediction | Force model, measured Cd, numerical checks, sensitivity, both flight comparisons | Assumption list, checks, comparisons, explanation of fitness for purpose |
| Requirements and tradeoffs | Sprint success criteria | Deployment altitude reference, direction, tolerance, action completion, packaging and mass | Requirement-to-test table and concept selection |
| Testing and uncertainty | Repeated sprint trials | Tunnel scatter, altitude characterization, software tests, integrated mechanism tests, flight evidence | Repeatability results, discrepancy analysis, supported pass/fail conclusions |
| Engineering responsibility | Individual preparation and shared decisions | Readiness arguments, configuration control, reporting limitations | Students explain why evidence supports a decision and what remains uncertain |

Brief discussions should arise from a decision students are making. Reserve occasional structured reflection to help students recognize that these practices apply beyond the rocket project.

## Model and instrumentation scope

### Flight model

Develop a vertical, one-dimensional model with supplied thrust data, constant gravity, a clearly stated constant-mass approximation, and drag that opposes velocity. Use the arithmetic mean of the designated wind-tunnel Cd values. Provide the environmental inputs and supported thrust-data import. Compare numerical results with a simple known case and smaller time steps.

The wind-tunnel lesson should establish the data range and any instrument-based exclusion rule in advance. Students calculate each Cd using force, density, speed, and reference area, then take the straight mean; curve fitting is outside the core assignment. Keep all original measurements and explain exclusions. The variation remains useful evidence about the limitations of representing drag with one coefficient.

Keep the preflight prediction unchanged as a record of what students expected. After flight, a separately labeled rerun using measured mass and flight-day conditions helps distinguish input errors from model limitations. Do not present a post-flight rerun as the original prediction.

Use Python in Jupyter for flight prediction and analysis. Use the Arduino framework with supported starter firmware for the instrument and actuator. Retain the existing PlatformIO-based workflow as the starting point; finalize the classroom installation and hardware configuration before lesson development.

### Instrumentation and deployment

Teach the signal path from sensor to stored measurement before asking students to modify flight-event logic. Characterize the complete package on battery power and verify that its saved data can be read and interpreted. Set measurement acceptance criteria that support the deployment requirement.

The deployment requirement must specify the altitude reference, ascent or descent, tolerance, allowed operating states, and the observable physical action. Recording an activation command is evidence of software behavior; demonstrating physical completion requires an additional observation or measurement. Consider sensor error, sampling, and actuator delay together when choosing a feasible tolerance.

Provide the applicable launch procedures and teach students to execute and question them. Use concise readiness records and observed performance rather than assigning students to author a separate launch procedure. Local launch operating requirements must be established for the actual vehicle and site; the Engr 201 handouts do not establish current operating limits.

## Communication and assessment

### Proposed group paper

Use a short technical report organized around the problem, approach, evidence, and conclusions. Set the final length after testing the assignment; a starting target is six to eight pages of main text and figures, with code and detailed test records linked separately. Use one supported template and prioritize technical clarity over elaborate formatting.

| Checkpoint | Lesson | Content added or revised |
| --- | --- | --- |
| 1 | 13 | Flight model, important assumptions, predicted trajectory, and model checks |
| 2 | 19 | Instrument package, altitude reference, and characterization evidence |
| 3 | 23 | First-flight comparison, discrepancy analysis, and implications for deployment |
| 4 | 30 | Deployment requirements, selected concept, rationale, and verification plan |
| Final | 39–40 | Both flight results, completed requirement assessment, conclusions, and recommendation |

Each checkpoint revises the same report. Readiness discussions, test records, and notebook work supply its evidence rather than creating duplicate reports. Give peer reviewers a narrow technical task, such as checking whether a figure supports its accompanying conclusion.

### Proposed assessment structure

Assess collaborative engineering through the project while collecting most graded evidence from supervised individual work on paper with a calculator. The following allocation uses 80% as a conservative planning assumption until the required percentage is finalized. Being physically in class does not make assisted group work eligible for the independent category. Online preflights also fall outside that category.

| Assessment | Course weight | Conditions |
| --- | --- | --- |
| Test 1 | 12% | Supervised individual work, lesson 14 |
| Test 2 | 12% | Supervised individual work, lesson 23 |
| Test 3 | 12% | Supervised individual work, lesson 33 |
| Cumulative final | 19% | Paper, pencil, and calculator; separate official exam slot to be confirmed |
| Five individual application checks | 25% total, 5% each | Paper-and-calculator tasks embedded in lessons 6, 11, 18, 28, and 38 |
| Group project work | 20% | Proposed split: sprint 3%, Rocket 1 evidence 5%, Rocket 2 design and test evidence 7%, final group paper and briefing 5% |
| Total | 100% | 80% supervised individual evidence; 20% collaborative project evidence |

This makes examinations 55% of the grade and individual applications 25%. Application checks should ask students to do engineering work: interpret a provided plot in lesson 6, calculate and interpret mean Cd in lesson 11, diagnose an instrumentation record in lesson 18, reason through an actuator interface in lesson 28, and assess a requirement from flight evidence in lesson 38. Schedule approximately 20–30 minutes for each, with earlier practice and no concurrent instructor coaching. Provide common data or equivalent tasks so assessment does not depend on whether a student's group hardware succeeded. In lesson 6, teach and practice the assessed notebook and plot basics before the independent check.

Design counted independent tasks for paper, pencil, and calculator. Supply plots, short printed code fragments, diagrams, and necessary question data so students can interpret and reason without using a computer. Set reference-sheet rules before publishing assessments. Instructor explanations, peer collaboration, and computer-based work remain part of ordinary learning activities; clearly distinguish those activities from independently graded assessment periods. Paper assessment can demonstrate algorithmic reasoning and interpretation but cannot alone establish that a student can operate the development tools or integrate hardware; observe those capabilities during the project as well.

Use common tasks and rubrics across the two sections, with equivalent variants if their meeting times create exposure concerns. For 40 students, five checks create 200 short responses across the semester. Constrain each to a few assessable decisions, use analytic partial-credit rubrics, and compare a small sample between instructors before splitting the marking. Choose assessment weights before publishing the syllabus; avoid changing them in response to individual results.

Judge project work on problem framing, technical reasoning, quality of evidence, appropriate interpretation, integration, and communication. A successful flight alone is insufficient evidence of learning. A failed test can support strong analysis, but students must still demonstrate required technical capabilities through follow-up work or an individual assessment.

### Course test development plan

The lesson placements below are proposed. Each of the three term tests has a complete two-hour meeting reserved; actual test duration remains to be decided. Use paper, pencil, and calculator, with reference-sheet rules to be set. The final has a separate official exam slot. Provide practice in the same kinds of reasoning during earlier lessons, and use the openings of lessons 15, 24, and 34 for brief feedback on common errors.

| Test | Coverage | Suggested tasks |
| --- | --- | --- |
| Test 1, lesson 14 | Lessons 1–13: problem framing, models, units, forces, numerical integration, wind-tunnel data, and interpretation | Improve an ambiguous requirement; draw and use a force diagram; calculate a few numerical steps; compute and average Cd from supplied valid data; diagnose an implausible plot or modeling assumption |
| Test 2, lesson 23 | Lessons 15–22, with essential modeling concepts revisited: instrumentation, event recognition, and first-flight comparison | Interpret altitude-reference and repeatability data; trace short event logic; compare flight and prediction; distinguish plausible explanations; respond to an evidence-reporting dilemma |
| Test 3, lesson 33 | Lessons 24–32, with earlier fundamentals revisited: deployment requirements, concept selection, mechanism and actuator reasoning, integration, and ground verification | Improve an ambiguous requirement; evaluate concepts; interpret actuator data; trace deployment logic; select tests distinguishing a command from completed physical action |
| Final, separate official exam slot | Cumulative reasoning, including second-flight evidence and transfer beyond the rocket | Evaluate a small unfamiliar system using supplied equations and diagrams; reconcile model and measurement; determine which requirements the evidence supports; recommend the next useful test |

For each test, develop an outcome-to-item blueprint before writing questions. Set the intended reasoning, points, expected completion time, prerequisite knowledge, and permitted tools. Draft the questions and worked solutions together, then create a partial-credit rubric and identify likely misconceptions. Review for ambiguous wording, dependence between questions, accessibility to all majors, and consistency with what students practiced. Solve and time the complete test before release; prepare an equivalent alternate form if needed.

Favor small calculations, diagrams, data interpretation, short code tracing or debugging, and justified decisions. Avoid making memorized syntax or a student's team role the main determinant of performance. Supply hardware details and equations when recalling them is outside the assessed outcome. Assess teamwork itself through observed team work and reflection; a written test can assess reasoning about a team situation but does not demonstrate teamwork performance.

Test questions, worked solutions, scoring rubrics, practice questions, and alternate forms are future development deliverables. Begin with Test 1 after agreeing on its blueprint and resource policy. Keep instructor keys separate from student versions when creating those materials.

The three term tests require supported firmware in lessons 15–16, a combined deployment-requirements and concept lesson 24, and focused corrections alongside notebook updates in lesson 34. Individual checks also use portions of five meetings. Preserve build and troubleshooting time within lessons 26 and 31–32, keep paper preparation brief, and reduce Rocket 2 technical scope if needed rather than consuming assessment or launch-contingency meetings.

## Daily online preflights

Provide a required preflight for each of the 41 lessons, including the first lesson, field trips, launch days, and term-test days. Blackboard is the expected platform. Deliver the first preflight with joining instructions early enough that students can complete it before the first meeting. If a lesson changes purpose because of weather, update its preparation rather than adding another assignment.

### Proposed format

Keep the entire preparation task to about 5–10 minutes on an ordinary day: a short reading, diagram, worked example, or video excerpt followed by three or four automatically scored questions. One question retrieves a recent concept; the others prepare students for the next activity. On test days, use a shorter two-question retrieval exercise without new content. The final-exam preparation is separate from the 41 daily preflights.

Use selected-response and simple numerical items with clear units and tolerances where supported. Avoid essays and uploads that require daily manual marking. A submission records completion even when some answers are wrong; retain the score as diagnostic information. The proposed default is required completion with zero course-grade weight, pending confirmation that the homework mandate permits that arrangement. If points are required, place them within the portion of the grade outside supervised independent assessment; do not add them to the independent 80% or increase the total above 100%.

Proposed settings are two attempts, automated explanatory feedback after submission, and a due time before each section's class. Keep a late route available for completing the requirement while preserving the original deadline for preparation records. Confirm how the local Blackboard configuration reports submissions, lateness, scores, and attempts before relying on an automated completion rule. Acknowledging readiness or clicking a pledge is insufficient as the entire homework; ask students to retrieve or apply something.

Keep preflights separate from the secure paper-test bank. Their purpose is preparation and feedback, not proof of unaided mastery. Publish an explicit resource policy for preflights; online homework cannot substantiate the no-assistance condition used for the independently earned grade.

### Blackboard implementation

Start with Blackboard's native assessment tools and a reusable lesson template. Blackboard documents supported [question types](https://help.anthology.com/blackboard/instructor/en/assessments/questions/question-types.html) and reusable [question banks](https://help.anthology.com/blackboard/instructor/en/assessments/questions/reuse-questions/question-banks.html). Confirm whether the Academy course uses Ultra or Original before generating import files or detailed setup instructions. Do not build a separate web application for the initial offering.

Maintain an editable master bank with these fields: lesson number, preparation material, objective, question identifier, prompt, response options or numerical answer, units/tolerance, correct answer, explanatory feedback, and revision status. Map question identifiers to their Blackboard items so corrections remain traceable. Validate one complete preflight in student preview before importing or copying a larger batch; verify grading, feedback, retries, deadlines for both sections, and the instructor's completion view.

Prepare the first ten preflights before launch of the course, using the existing sprint handouts for lessons 1–4. Develop later preflights alongside their lessons, maintaining the same four-lesson preparation lead as the teaching materials. If each has three or four questions, the course needs approximately 123–164 items before any variants, so prioritize a small reliable bank over large randomized pools.

### Example preflight for lesson 7

Preparation: a short illustrated explanation of a signed force sum and F=ma. These questions illustrate the format; the final examples should match instruction and the selected convention.

1. With upward positive, a 0.50 kg rocket has 8.0 N upward thrust, 1.0 N downward drag, and 4.9 N downward weight. What is its net force? Correct answer: +2.1 N. Feedback: add signed forces, 8.0 - 1.0 - 4.9.
2. For the same instant, what is its acceleration? Correct answer: +4.2 m/s². Feedback: use net force divided by mass, not thrust divided by mass.
3. After motor burnout, the rocket is still traveling upward. Which way does drag act? Correct answer: downward. Feedback: drag opposes motion relative to the air; it does not always point downward during the entire flight.

Use the results to choose a brief opening explanation. Students who miss a question should arrive with feedback they can use; an instructor should not have to hand-grade daily homework for 40 students.

## Meeting pattern and schedule resilience

A useful two-hour default is 10 minutes to retrieve prior learning and establish the question, 20 minutes of instruction or demonstration, 65 minutes of student work, 15 minutes comparing results, and 10 minutes documenting decisions and next steps. Adjust for field trips, fabrication, and launch operations.

Use lesson numbers for dependencies rather than assuming a fixed number of meetings each week. Checkpoint submissions should follow completion of the relevant activity when the calendar shifts. Lessons 21 and 37 are protected contingency meetings. If unused for launch, use them for targeted testing and analysis rather than adding new required content.

If flight evidence is unavailable, provide a common flight dataset for the analysis objectives, while recording which student hardware and mechanism objectives remain undemonstrated. A supplied dataset does not demonstrate that a team's hardware worked. Confirm whether launch logistics fit a two-hour meeting or require coordinated scheduling.

## Relationship to the engineering sequence

Engr 101 establishes common practices in requirements, models, measurements, computation, design, tests, teamwork, and communication. Subsequent courses can revisit them through energy in a driving vehicle, power in a flying vehicle, systems in a space vehicle, and the capstone. Record demonstrated exit capabilities during this experimental offering for use when the lead begins Engr 202 development in late spring or summer. Engr 202 planning is not a startup dependency.

The current map introduces systems thinking through interfaces and integrated behavior without attempting the depth of the later systems course. It similarly uses energy and electrical power where needed without taking over the later courses' central content.

## Engr 201 material to adapt

| Private remote source | Use in Engr 101 |
| --- | --- |
| [Syllabus](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/SYLLABUS.MD) | Reference for existing activities and communication sequence; policies require separate course decisions |
| [Rocket prediction](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/rocket_prediction/ASSIGNMENT_INSTRUCTIONS.md) | Adapt estimate, force balance, numerical trajectory, and plots to a scaffolded notebook; replace fitted Cd with its arithmetic mean |
| [Rocket prediction algorithm](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/rocket_prediction/rocket_prediction_algorithm.md) | Starting point for sequencing the flight calculation; reconcile update conventions and correct notation before reuse |
| [Modeling notes](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/notes/06%20modeling.md) and [numerical integration notes](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/notes/07%20numerical%20integration.md) | Rebuild around freshman preparation, force diagrams, rates, and accumulation; verify equations before conversion |
| [Arduino introduction](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/arduino_intro/ASSIGNMENT_INSTRUCTIONS.md) | Adapt upload, simple modifications, and nonblocking timing examples |
| [Rocket instrumentation](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/rocket_instrumentation/ASSIGNMENT_INSTRUCTIONS.md) | Adapt acquisition, battery operation, altitude tests, and flight-event logic; extend toward verified actuation |
| [Rocket launch](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/rocket_launch/ASSIGNMENT_INSTRUCTIONS.md) | Retain readiness reasoning and quick-look communication; provide procedures rather than assigning procedure authorship |
| [Technical paper](https://github.com/usafa-engr-201/engr-201/blob/b307a9e96fa7d3dbdfb82caf2f1197efcedc867d/assignments/paper/ASSIGNMENT_INSTRUCTIONS.md) | Simplify into a group report with progressive revision and a deployment design argument |

Atmosphere-calculator development, Simulink, and the discipline-specific Aero/Astro blocks are outside this map. The proportion reused should be measured against agreed outcomes and instructional time rather than file count.

## Decisions before detailed lesson development

1. Obtain the existing sprint materials and confirm its instructor handoff.
2. Confirm the final independent-assessment percentage, reference-sheet rules, weights, and official final-exam arrangements; confirm Blackboard course version and whether completion-only homework meets the preflight requirement.
3. Prepare lessons 5–10, introductory net-force instruction, and the supported notebook environment without relying on Science 1 sequencing.
4. Verify the existing Rocket 1 hardware and software workflow and establish a mass estimate and flight-model baseline for the approximately 600 mm D12 vehicle and desired 100 m maximum altitude.
5. Set Rocket 2 scope and feasible deployment requirements during the semester, before the student design phase.
6. Confirm equipment distribution among ten proposed teams, fabrication support, and launch logistics for two sections.

## Preparation for the experimental offering

Use the roughly three-week preparation window identified by the lead as a work budget, with 6 January 2027 as the fixed start. Develop a dependable opening and assessment structure, then maintain a rolling preparation lead. Detailed Rocket 2 development and Engr 202 development can follow later.

| Preparation period | Priority deliverables | Suggested responsibility |
| --- | --- | --- |
| Week 1 | Adopt sprint materials; confirm assessment interpretation; publish course outcomes, provisional schedule, grading, and resource rules; choose and test the notebook delivery environment; verify one Blackboard preflight template | Lead coordinates course and policy; sprint instructor supplies established opening materials |
| Week 2 | Complete lesson 5 and lessons 6–10; run the notebook from a clean student setup; prepare force-balance examples, tunnel data sheet, first application check with rubric, and preflights for lessons 1–10 | Lead develops modeling sequence; co-instructor trials the student workflow, preflights, and tunnel activity |
| Week 3 | Rehearse the opening technical lessons; finish lessons 11–14 at draft level, including Test 1 blueprint, practice, candidate items, and key; verify Rocket 1 equipment and supported firmware; agree on common assessment rubrics | Both instructors review the opening and sample marking; divide hardware and assessment preparation explicitly |

Before day one, lessons 1–5 should be ready to teach, lessons 6–10 should be runnable and reviewed, and the rest of Rocket 1 should have a viable technical path. Have a complete Test 1 blueprint and a draft of its questions and solutions, then review it against instruction actually delivered before use. There is no need to finish every later slide deck or test form before the semester begins.

During the semester, use a short weekly instructor meeting to review student evidence, agree on the next lessons, and record changes for both sections. Aim to keep teaching materials four lessons ahead and assessment materials far enough ahead for independent review. Use the four established sprint meetings to finish the opening rocket lessons rather than redesigning the sprint.

Develop the later course by milestones: prepare the Rocket 1 analysis dataset and workflow before first launch; demonstrate a feasible Rocket 2 mechanism, actuator interface, and trigger test before releasing its assignment around lesson 24; complete each later test and rubric in time for review. If Rocket 2 feasibility slips, reduce the mechanism's complexity and retain requirements, concept selection, integration, and verification as the instructional core. A ground demonstration can supply assessed engineering evidence if flight integration cannot be completed, but the intended second flight remains the course target and an unflown system must be reported as such.
