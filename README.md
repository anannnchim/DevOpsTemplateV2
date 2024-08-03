

**Phase 1**

Make the project as a package and install that package as enviornment.

`src/function` A folder of functions.

`tests/test_function.py` A test file

`pyproject.toml` The old way to install a package.

`setup.py` An installation script. 

`setup.cgf` A configuration file to store metadata. 

`requirement.txt` All dependencies with version - to run the project. 

Then run `Then pip install -e .` in terminal-push a link to src directory.

**Phase 2**

Make a project be able to test with several virtual environment. 

`requirements_dev.txt` A requirement to run a test. 

`setup.cfg` Modify - Add requirement information from above file.

`src/function/py.typed` Add empty file

`pyproject.toml` - Add configuration for pytest and mypy

Then run `pip install -r requirements_dev.txt` in terminal to install.

Check if we set up correctly by:
- Run `mypy src` , `flake8 src`, `pytest` if there is no issue

`tox.ini` A configuration file that will make sure that allow us to create new virtual environment and install those package into it, and run test.

Run the commands `tox` in the terminal (`rm -rf .tox` to remove)

Note: given pytest
- folder should be `tests`
- file should start with `test_function`
- function inside a file start with `test`


**Phase 3**

Connect with Github Action

`.github/workflows/tests.yml` Add it

`tox.ini` Add github section


![Tests](https://github.com/anannnchim/DevOpsTemplateV2/actions/workflows/tests.yml/badge.svg)