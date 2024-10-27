# Example of using uv

This project structure includes a set of shared dependencies in a `general_requirements.txt` file, which are common across multiple projects. The setup consists of two main components:

1. **Utility Library (`util_lib`)**: A library containing general-purpose functions and tools.
2. **Main Library (`actual_lib`)**: The primary project that depends on `util_lib` and uses its functionalities.

Both `util_lib` and `actual_lib` may rely on dependencies defined in the shared `requirements.txt`.

## Scenario

Say you have your `general_requirements.txt` somewhere in the system (here put it at root)

### 0. install python with uv

```bash
# numpy/pandas doesn't support well for > 3.11 at the moment
# so just use 3.11 in the example

uv python install 3.11 # if you haven't installed
uv python pin 3.11 # as uv default, if you want
```

### 1. setup util_lib

```bash
uv init --lib util_lib
cd util_lib
#--------------------------------
uv venv
source .venv/bin/activate
#--------------------------------
touch src/print_general_deps.py # put the content accordingly
#--------------------------------
uv pip install -r ../general_requirements.txt
```

### 2. Set up the main project

```bash
uv init --lib main_project
cd main_project
#--------------------------------
uv venv
source .venv/bin/activate
#--------------------------------
touch src/print_general_deps.py
#--------------------------------
uv pip install -r ../general_requirements.txt
uv pip install -e ../util_lib
# or if from github, should be something like
# uv install git+https://github.com/yourusername/util_lib.git
uv run src/main_project/project_main.py
```

## Maintaining shared dependencies

### Benefits of Project-Specific Installation

1. **Environment Isolation**:
   - Installing `general_requirements.txt` within each project’s virtual environment (e.g., one for `util_lib`, another for `main_lib`) keeps each project self-contained.
   - This isolation avoids dependency conflicts, allowing each project to operate independently, even with future updates or changes to dependencies.

2. **Version Compatibility**:
   - If `util_lib` and `main_lib` eventually require different versions of the same package, isolated environments allow each project to maintain its unique compatibility requirements.
   - This approach minimizes the risk of dependency issues that might arise when updating or adding packages across projects.

3. **Reproducibility**:
   - Project-specific environments make reproducing your setup easier, whether for collaborators, CI/CD, or deployment. Each project specifies its requirements independently, avoiding reliance on global installations.

---

### Cases for Global Installation

Installing `general_requirements.txt` globally might be beneficial in specific, limited scenarios:

- **Disk Space Concerns**: If disk space is very constrained, global installation could save space. However, this sacrifices isolation and is generally not recommended in development environments.
- **Single-Use Workflow**: If `util_lib` and `main_lib` are always used together and not distributed or used independently, a global setup might be sufficient.

---

### To ensure consistency in dependencies across projects

- Update `general_requirements.txt` with any changes to shared dependencies.
- Re-run `uv install -r ../general_requirements.txt` in each project as needed.
