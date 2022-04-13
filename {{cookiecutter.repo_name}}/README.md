# {{cookiecutter.project_name}}
This repo contains the implementation of a backend-service  suitable for a project.

## How to run it:
The following instructions are based on a UNIX-based system.

1. Clone this repo.
2. On a terminal run: `python3 -m pip install -U poetry`
3. Also run: `poetry install` from within this project's root folder.
4. After install all dependencies, you'll have a clean instalation ready for use.
5. Run `poetry run uvicorn mission_control:app` to simply start the server.

## How to develop:
The included settings under `.vscode` provide a suitable base config for anyone who shall touch this code base.
`launch.json` Provides 3 types of debugging mode:
   - `mission_control`: will run the debugger starting from the `mission_control.py` file this is optimal for testing code not related to the server but in the same workflow. Eg: database setup, config loading.
   - `FastAPI`: will run the server in production (using uvicorn) which lets you assure the proper handling of production evironments.
   - `current file`: This is intender for idea testing purposed, as it only runs the file from which you call the debugger. It will not run the entire application.

`settings.json` Provides configuration for the test framework of choice `Pytest` as well as the static code analyzed `Mypy`, the environment in which to load the modules and some other settings.

Any new piece of code should be covered by at least one unit test, of course this is not a requirement but a simple ask. As well, a the next one.... being adecute with the domain structured priciples followed by this team.


It should be noticed, the team imposes the PEP8 format style by a workflow which runs in every PR. Meanign you should not worry about code style as long as that workflow propely runs.

## Tests:
The `test/` folder contains a suite of unit tests which aims to cover the largest amoun of production code possible. Tests, are defined in any 
python file (`.py`) which contains the prefix `test_` and the name of the funcion inside starts with the word `test_`. This are mere 
requirements imposed by the framework of choice. The `conftest.py` file is special, it contains the the defintion of `fixtures` which are 
simply arguments of the test suite. `Pytest` handles Dependency Injection on it's own which might have some issues with `dependency-injector`
but those are simply avoidables. 
Example:
```
# conftest.py: 
from pytest import fixture
from fastapi.testclient import TestClient
from {{cookiecutter.project_name}} import app

@fixture()
def test_username() -> str:
    return 'test_name'

@fixture()
def test_app(settings: AppConfig) -> TestClient:
    return TestClient(app)

```
```
# test_user_creation.py

from fastapi.testclient import TestClient

def test_create_user(test_client: TestClient, test_username: str) -> None:
    result = test_client.post('/user/', json = {'username': test_username ...})
    yield result.ok, 'If this messege get's displayed it means the test failed'


```

To run the entire test suite, simply run `poetry run pytest tests`
