# CI-CD-builder

Fast API CI/CD project for Github Actions

This FastAPI application provides a health endpoint and analyzes submitted text to calculate character and word counts. GitHub Actions installs dependencies, checks dependency compatibility, and runs automated tests against pushed commits and pull requests. Render automatically deploys changes to main after CI checks pass.

Note: Manual deployments bypass the automatic CI gate, so verify that the selected commit has passed CI before deploying manually.

## Local setup

Requires Python 3.14. Run these commands from the project folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to try the API.
Stop the server with Ctrl+C.

## Run tests

From the project folder in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

The tests cover the health endpoint, text analysis, missing text, non-string
input, empty text, and extra whitespace. A running Uvicorn server is not
required because the tests use FastAPI's TestClient.
