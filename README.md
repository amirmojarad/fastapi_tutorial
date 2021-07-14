# FastAPI Tutorial
## [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
### installation and Run

to install FastAPI run this line in Termianl/Powershell
` pip install fastapi[all] `

Run the live server:

` uvicorn main:app --reload `

The command `uvicorn main:app ` refers to:

* `main`: the file `main.py` (the Python "module")
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`
* `--reload`: make the server restart after code changes. Only use for development

Your Project is Available in `http://127.0.0.1:8000`

### Points
* `@app.get("/")` :  this decorator tells FastAPI that the function below corresponds to the path `/` with an operation `GET`.

## [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
