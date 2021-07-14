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
### Code
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is Running! ... "}

```
## [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
### Path Parameters
```python
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
The value of the path parameter `item_id` will be passed to your function as the argument `item_id`

### Path parameters with types
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
* This will give you editor support inside of your function, with error checks, completion, etc.

### Code
```python
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is Running! ... "}


@app.get("/items/id/{item_id}")
async def read_id(item_id: int):
    return {"item_id": item_id}


@app.get("/items/name/{item_name}")
async def read_name(item_name: str):
    return {"item name": item_name.upper()}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resent = "resent"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    message = ""
    if model_name == ModelName.alexnet:
        message = "Deep Learning!"
    elif model_name == ModelName.lenet:
        message = "LeCNN all the images"
    else:
        message = "Have some residuals"
    return {"model_name": model_name, "message": message}
```
