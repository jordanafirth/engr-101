# Engr 101 Course Development

Planning materials for the experimental introductory engineering course at the US Air Force Academy, beginning 6 January 2027. The course serves all majors and opens a five-course integrated engineering sequence.

## Start here

1. Read [the handoff summary](docs/handoff.md) for decisions, current status, and the next development priorities.
2. Read [the course design and 41-lesson map](engr-101-course-map.md) for the detailed working proposal.
3. Use [the development backlog](docs/development-backlog.md) to select the next concrete deliverable.
4. Consult [the source guide](docs/sources.md) for the private Engr 201 reference repository and access instructions.
5. Open [the guided D12 rocket-prediction project](projects/rocket_prediction/README.md) for the first executable student notebook and worked teaching example.

## Continue on another computer

Clone this repository using a GitHub account with access:

```sh
git clone https://github.com/jordanafirth/engr-101.git
cd engr-101
```

Open the cloned folder in your coding assistant or editor. No Python environment or firmware installation is needed to read and edit the planning documents. For notebooks, install [Pixi](https://pixi.prefix.dev/latest/installation/), then run these commands from the repository root:

```sh
pixi install --locked
pixi run lab
```

The manifest and lockfile define the course environment. Use `pixi run check` for the project validation checks. See the project README for installation validation status and teaching scope.

The private Engr 201 source is a separate repository. Authenticate an authorized GitHub account on the new computer before accessing it; see the source guide. This repository includes small normalized D12/tunnel teaching datasets with provenance, rather than a snapshot of that course. Student records and the personal-background document are not included.

Suggested opening prompt for a new chat:

> Continue developing Engr 101. Read README.md, docs/handoff.md, docs/development-backlog.md, and engr-101-course-map.md. Treat the user's established decisions separately from proposals. Do not redesign the existing sprint. Review the guided D12 notebook in projects/rocket_prediction and its validation status. Prioritize lesson 5 and lessons 6–10, with daily Blackboard preflights and paper-and-calculator assessment. Consult docs/sources.md for Engr 201 references. Full lesson packages and examinations remain to be built.

Commit and push changes before switching computers. On the other computer, pull before editing an existing clone.

## Status

The repository contains a planning draft, handoff materials, and a guided D12 prediction notebook with a worked teaching example and validation tools. Full lesson packages, new firmware, Blackboard imports, and complete examinations and answer keys remain to be developed. The detailed map labels proposed choices; neither the tentative grading allocation nor every lesson placement is a finalized course policy.
