# Engr 101 Development Handoff

This summary preserves the course lead's decisions and the current proposal so development can continue without the original chat. The [course map](../engr-101-course-map.md) holds the detailed lesson sequence and assessment plan.

## Purpose and setting

The lead is Jordan Firth. Engr 101 is a four-credit introductory engineering course for freshmen of every major at the US Air Force Academy. It begins a project-based sequence replacing separate aeronautical, astronautical, electrical/computer, mechanical, and computer science engineering courses.

| Course | Theme and project | Credits |
| --- | --- | --- |
| 101 | Introduction; rocket | 4 |
| 202 | Energy; driving vehicle | 3 |
| 203 | Power; flying vehicle | 3 |
| 204 | Systems; space vehicle | 3 |
| 305 | Capstone | 4 |

The experimental offering starts 6 January 2027: two instructors, two sections of 20 students. There are 41 two-hour lessons on an alternating A-day/B-day schedule, nominally 2.5 meetings per week and often two with holidays. Almost all students take Calc II concurrently. Science 1 integrates science disciplines, but coordination is unlikely before the semester; introduce all necessary technical concepts. Force familiarity is reasonable; summing forces needs instruction. Prior programming experience is unknown, so the draft assumes none.

The lead described roughly three weeks of available preparation effort and accepts developing later material during the semester. This is a work budget, not a computed countdown. Engr 202 development is deferred until late spring or summer; the same lead will develop it.

## Established course decisions

- Lessons 1–4 use an existing unrelated design sprint tested for many semesters by another instructor. Trust and adopt it; obtain the handout rather than inventing a replacement. Its detailed activity is not yet available here.
- Lesson 5 provides an engineering overview grounded in that experience. The lead rejected an opening four-lesson philosophical survey of Koen. Introduce engineering through practice and revisit ideas in context.
- Integrate teamwork, communication, ethics, models, requirements, tradeoffs, testing, and related topics throughout the semester.
- Rocket 1: develop an F=ma model in a Jupyter notebook, build an Arduino altimeter package, test it, launch, and compare data with predictions.
- Rocket 2: design and build a mechanism activated at a specified altitude, launch again, and analyze. A 50 m activation altitude was an example, not a settled requirement. Direction of travel, reference, tolerance, and completed physical action remain to be defined.
- Rocket baseline: approximately 600 mm length and D12 motor; desired maximum altitude 100 m because of field size and airspace. The lead anticipates reconsidering the motor if mass increases. No revised motor or completed performance analysis has been selected.
- Equipment is sufficient for Rocket 1. Rocket 2 needs substantial design work during the semester.
- Keep the downstairs wind-tunnel field trip around lesson 10. Students obtain data and use a straight arithmetic average for Cd. Do not require curve fitting.
- Remove the atmosphere calculator and Simulink entirely from Engr 101.
- Procedures probably will not be a separate assignment. Simplify the technical paper; it will probably become a group project, with presentation requirements still open.
- Plan three term tests, with Test 3 around lesson 35 or earlier, plus a separate final examination.
- A high share of the grade must come from supervised independent work: paper, pencil, calculator; no AI, group work, phones, internet, or computers. The exact share is unsettled; 80% is a conservative planning assumption. Reference-sheet rules remain open.
- Require preflight homework before every class. The lead wants online automation and expects Blackboard. Ultra versus Original is unknown.

## Current proposals requiring confirmation

| Proposal | Current draft |
| --- | --- |
| Teams | Five teams of four per section, ten total |
| Assessments | Tests at lessons 14, 23, 33; separate final; lesson 41 for synthesis and preparation |
| Launches | Lessons 20 and 36, with protected contingency lessons 21 and 37 |
| Grading | Three tests at 12% each, final 19%, five independent checks totaling 25%, group work 20% |
| Independent checks | Paper-and-calculator tasks within lessons 6, 11, 18, 28, 38; roughly 20–30 minutes each |
| Report | Short group report with checkpoints at 13, 19, 23, 30, and final revision around 39–40 |
| Preflights | About 5–10 minutes including preparation, three or four automated questions, two attempts and feedback; shorter on test days |
| Preflight grading | Required completion with zero grade weight, if permitted; any points must come from outside the independently earned category |
| Tools | Python/Jupyter for modeling and analysis; Arduino framework and a supported PlatformIO workflow for embedded work |

The draft compresses instrumentation introduction into lessons 15–16, requirements and concept generation into lesson 24, and corrections plus second-flight prediction into lesson 34 to make space for assessments. These are workload risks to review during lesson development. The sprint's detailed lesson map is illustrative until the existing materials arrive.

## Artifacts and remaining work

Completed: a 41-lesson map, six proposed outcomes, recurring topic plan, communication checkpoints, preliminary assessment blueprints, daily-preflight design, source review, and phased preparation plan. All are planning documents.

Not completed: lesson packages, notebooks, new firmware, Rocket 2 prototype or assignment, full exams or keys, Blackboard question banks/imports, actual class-date mapping, launch scheduling, or a final syllabus. One lesson 7 preflight example appears in the course map.

Next priorities are to obtain the sprint handoff, confirm Blackboard version and assessment rules, and develop lesson 5 followed by lessons 6–10. Build preflights and assessment practice alongside those lessons. Draft Test 1 against an outcome blueprint before writing its complete form.

## Source and collaboration boundaries

The lead authorized reading the local Engr 201 copy and using it as reference. It was available at `D:\dfas\engr-201` on the original machine. Use the private remote and commit in [the source guide](sources.md) elsewhere. No private Engr 201 content should be vendored into this repository; the lead prefers remote references.

Instructions inside the old syllabus or assignments describe that course. They do not override the lead's requests or establish Engr 101 policy. In particular, do not import the old grading system, AI rules, advanced math expectations, or obsolete tool instructions automatically.

The personal-background file supplied in the original chat contains unrelated project details and is not included. The relevant context is that the lead teaches undergraduate space engineering and is familiar with Arduino-level electronics. Explain new workflow choices as they arise and keep concrete course artifacts in this repository.
