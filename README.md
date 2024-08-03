## Project Setup and Testing Phases

### Phase 1: Package Setup and Installation

1. **Project Structure**:
    - `src/function`: A folder containing your function modules.
    - `tests/test_function.py`: A file containing your test cases.
    - `pyproject.toml`: Configuration file for modern package management.
    - `setup.py`: Installation script for the package.
    - `setup.cfg`: Configuration file to store metadata.
    - `requirements.txt`: List of dependencies required to run the project.

2. **Steps**:
    - Run the following command in the terminal to install the package in editable mode:
      ```sh
      pip install -e .
      ```

### Phase 2: Testing with Multiple Virtual Environments

1. **Files and Configuration**:
    - `requirements_dev.txt`: List of dependencies required for running tests.
    - `setup.cfg`: Modify to include requirement information from `requirements_dev.txt`.
    - `src/function/py.typed`: Add an empty `py.typed` file to signal that the package contains type hints.
    - `pyproject.toml`: Add configuration for `pytest` and `mypy`.

2. **Installation and Setup**:
    - Run the following command to install the development dependencies:
      ```sh
      pip install -r requirements_dev.txt
      ```

3. **Verification**:
    - Run the following commands to ensure the setup is correct:
      ```sh
      mypy src
      flake8 src
      pytest
      ```

4. **Tox Configuration**:
    - `tox.ini`: Configuration file to create new virtual environments, install packages, and run tests.

5. **Run Tox**:
    - Run the following command to execute tests in multiple environments:
      ```sh
      tox
      ```

    - If necessary, remove existing virtual environments with:
      ```sh
      rm -rf .tox
      ```

**Note**: For `pytest`, ensure the following conventions:
- The test folder should be named `tests`.
- Test files should start with `test_`.
- Functions inside test files should start with `test_`.

### Phase 3: Continuous Integration with GitHub Actions

1. **GitHub Actions Configuration**:
    - `.github/workflows/tests.yml`: Add this file to configure GitHub Actions for continuous integration.

2. **Tox Configuration for GitHub Actions**:
    - Modify `tox.ini` to include a section for GitHub Actions.

3. **Badge for README**:
    - Add the following badge to your `README.md` to display the status of your GitHub Actions tests:
      ```markdown
      ![Tests](https://github.com/anannnchim/DevOpsTemplateV2/actions/workflows/tests.yml/badge.svg)
      ```

### General Note

- When adding a function, ensure to include both the function implementation file (e.g., `function.py`) and the corresponding test file (e.g., `test_function.py`).
