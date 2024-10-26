# Python Packaging

## Tools for Python Project and Dependency Management

| Feature                             | `pyenv`                         | `uv`                            | `Poetry`                      | `pipenv`                         | `virtualenv` + `pip`         |
|-------------------------------------|---------------------------------|---------------------------------|--------------------------------|----------------------------------|------------------------------|
| **Python Version Management**       | ✔️ Manages Python versions      | ✔️ Automatic with `.python-version` | ✖️ Integrates with `pyenv`  | ✖️ Integrates with `pyenv`       | ✖️                           |
| **Dependency Management**           | ✖️ Only manages versions        | ✔️ Fast resolution, lockfile      | ✔️ Lockfile and groups         | ✔️ Creates `Pipfile` with lock   | ✖️ Only installs dependencies |
| **Virtual Environment Support**     | Works with `virtualenv`         | ✔️ Creates `.venv` directory       | ✔️ Integrated and automatic    | ✔️ Automatic with virtualenv      | ✔️ Manual setup required     |
| **Packaging (sdist & wheel)**       | ✖️                               | ✔️ Builds for publishing          | ✔️ Builds and publishes         | Partial support for `pipenv`     | ✖️                           |
| **Publishing to PyPI**              | ✖️                               | ✔️ Publish directly               | ✔️ PyPI integration             | ✖️                               | ✖️                           |
| **Lock Files for Reproducibility**  | ✖️                               | ✔️ Universal lockfile             | ✔️ `poetry.lock` consistency    | ✔️ `Pipfile.lock`                 | ✖️                           |
| **Speed of Dependency Resolution**  | N/A                             | ⚡ Faster than most tools         | Moderate                       | Slower                            | N/A                          |
| **Third-party Tool Support**        | Extensive                       | Limited but growing              | Extensive                      | Moderate                          | Extensive                    |
| **Group Dependency Management**     | ✖️                               | Limited (only dev dependencies)  | ✔️ Custom groups                | ✖️                               | ✖️                           |
| **Ideal Use Case**                  | Multi-version Python projects   | All-in-one fast project setup    | Full project management         | Simplified isolated environments | Lightweight setups           |

### 1. **`pyenv` (Python Version Management)**

- **Purpose**: Manages multiple Python versions on a single machine.
- **Strengths**: Allows easy switching between Python versions and integrates well with `virtualenv` for isolated environments.
- **Limitations**: Focuses only on version control, without native dependency or packaging management.
- **Ideal Use**: Best suited for projects that require specific Python versions across different environments or for testing compatibility.

### 2. **`uv` (Rust-Based Project Manager)**

- **Purpose**: An all-in-one tool for managing dependencies, environments, and packaging; designed similarly to `Poetry` but written in Rust for enhanced performance.
- **Strengths**:
  - Faster dependency resolution due to its Rust foundation
  - Integrated virtual environment management, automatic support for `.python-version`
  - Project management from setup through publishing
- **Limitations**: Still gaining traction, with limited support from third-party tools.
- **Ideal Use**: Ideal for developers who want fast, comprehensive project management with minimal setup time.

### 3. **`Poetry` (Dependency and Packaging Manager)**

- **Purpose**: Manages dependencies, virtual environments, and packaging through a user-friendly interface.
- **Strengths**: Popular and well-supported, offering reproducible builds with lock files, dependency grouping, and automatic environment handling.
- **Limitations**: Slightly slower dependency resolution than `uv`, though very robust overall.
- **Ideal Use**: Effective for complete project workflows where dependency, packaging, and publishing are key requirements.

### 4. **`pipenv` (Combines `pip` and `virtualenv`)**

- **Purpose**: Manages dependencies and virtual environments using `Pipfile` and `Pipfile.lock`.
- **Strengths**: Easy to set up and use for isolated environments, combining `pip` and `virtualenv` functionality in one.
- **Limitations**: Slower dependency resolution and less comprehensive in project management capabilities compared to `Poetry` or `uv`.
- **Ideal Use**: Suitable for simpler setups where basic environment management and dependency handling are sufficient.

### 5. **`virtualenv` and `pip`**

- **Purpose**: `virtualenv` provides isolated environments, and `pip` installs packages.
- **Strengths**: Lightweight, minimal setup with broad compatibility, especially when used with `pyenv`.
- **Limitations**: Lacks built-in dependency management or lock file capabilities.
- **Ideal Use**: Ideal for minimalistic setups or custom environments where dependency isolation is needed without added complexity.

---

## Recommended Workflows

### **Comprehensive Project Management**

- **Tools**: `Poetry` or `uv`.
- **Scenario**: For developers needing end-to-end dependency, environment, and package management with easy publishing to PyPI.

### **Python Version Management with Dependency Control**

- **Tools**: `pyenv` + `virtualenv` or `Poetry`.
- **Scenario**: For projects requiring specific Python versions, with the flexibility of either isolated environments or full dependency management.

### **Lightweight Setup**

- **Tools**: `virtualenv` and `pip`.
- **Scenario**: Best for minimal dependency requirements and projects needing isolated environments without extensive setup.

---

## Packaging with `uv`, `Poetry`, and `pyenv`

### 1. **`uv`**

- **Building `sdist` and `wheel`**: Run `uv build` to create both distribution types in the `dist/` directory.
- **Publishing**: Use `uv publish` to upload the package to PyPI directly.

### 2. **Poetry**

- **Building `sdist` and `wheel`**: Run `poetry build` to generate both `sdist` and `wheel` files.
- **Publishing**: Use `poetry publish` to publish directly to PyPI.

### 3. **pyenv**

- **Usage**: Primarily manages Python versions; use with `setuptools`, `Poetry`, or `uv` for packaging and distribution.
- **Example with `setuptools`**:
  - Run `python setup.py sdist bdist_wheel` to create both `sdist` and `wheel` packages.

| Feature               | `uv`              | `Poetry`          | `pyenv`                             |
|-----------------------|-------------------|-------------------|-------------------------------------|
| `sdist` support       | `uv build`        | `poetry build`    | Use with `setuptools`               |
| `wheel` support       | `uv build`        | `poetry build`    | Use with `setuptools`               |
| Publishing            | `uv publish`      | `poetry publish`  | Not directly applicable             |

---

## Distribution Types: `sdist` vs. `wheel`

### **Source Distribution (sdist)**

- **Format**: `.tar.gz` or `.zip` archive with source code.
- **Uses**: Platform-independent, ideal for pure Python packages.
- **Scenarios for Only `sdist`**:
  - Packages with only Python code and no compiled extensions.
  - When source transparency and user customization are preferred.

### **Binary Distribution (Wheel)**

- **Format**: `.whl` (pre-built binary).
- **Uses**: Packages with compiled code or platform-specific dependencies.
- **Scenarios for Only `wheel`**:
  - Packages with complex dependencies or performance needs (e.g., C extensions).
  - Platform-specific binaries preferred for ease of installation.

---

## Installing a Local Project with `setuptools` in a `uv` Environment

### **1. Activate the `uv` Environment**

- Ensure your `uv` environment is active so `pip` installs packages within it.
- To activate, use:

  ```bash
  source .venv/bin/activate
  ```

  - Replace `.venv` with the name of the `uv` environment, if different.

### **2. Install the Local Package in Editable Mode**

- Use `pip` to install the package from the project’s root directory in editable mode:

  ```bash
  pip install -e /path/to/your/local/project
  ```

  - **Note**: The `-e` flag enables editable mode, so any changes in the source files reflect immediately without reinstalling.
  - **Path**: Ensure the provided path is the project’s root directory, where `setup.py` or `pyproject.toml` is located, not an `sdist` or `whl` file.

### **3. Verify the Installation**

- Confirm the package installation by listing installed packages:

  ```bash
  pip list
  ```

---

### How Editable Mode Works

- Using `pip install -e` directs `pip` to install in "editable mode." It reads the `setup.py` or `pyproject.toml` file in the specified directory to manage installation.
- **No Pre-built Package Required**: There’s no need to build an `sdist` or `wheel` file beforehand; `pip` handles this during installation.

### **Alternative Installation: Using `wheel` or `sdist` Directly**

- If you already have a built `.whl` or `.tar.gz` file, you can install it as follows:

  ```bash
  pip install /path/to/your/file.whl
  ```

  or

  ```bash
  pip install /path/to/your/file.tar.gz
  ```

---

### Summary

- **Editable Mode for Development**: `pip install -e /path/to/project_directory`
- **Direct Install from Built File**: `pip install /path/to/file.whl` or `pip install /path/to/file.tar.gz`
