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
