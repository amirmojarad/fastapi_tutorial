# FastAPI Tutorial

## installation and Run

to install FastAPI run this line in Termianl/Powershell
` pip install fastapi[all] `

Run the live server:

` uvicorn main:app --reload `

The command `uvicorn main:app ` refers to:

* `main`: the file `main.py` (the Python "module")
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`
* `--reload`: make the server restart after code changes. Only use for development

## Table of Contents

