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

* `@app.get("/")` :  this decorator tells FastAPI that the function below corresponds to the path `/` with an
  operation `GET`.

### Code

```python
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

## [Query Parametes](https://fastapi.tiangolo.com/tutorial/query-params/)

### Send Data as Query Parameter

` http://127.0.0.1:8000/items/?skip=0&limit=10 `

starts with `?` and declare query name, separate with `&`

send data with optional query parameter with essential query parameter

`http://127.0.0.1:8000/foo/1?q=query_parameter`

### Query parameter type conversion

`http://127.0.0.1:8000/items/foo?short=1`

`http://127.0.0.1:8000/items/foo?short=True`

`http://127.0.0.1:8000/items/foo?short=true`

`http://127.0.0.1:8000/items/foo?short=on`

`http://127.0.0.1:8000/items/foo?short=yes`

all above means `short = True`

### Required Query Parameter

When you declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not
required.

If you don't want to add a specific value but just make it optional, set the default as `None`.

But when you want to make a query parameter required, you can just not declare any default value:

## [Request Body](https://fastapi.tiangolo.com/tutorial/body/)

## [Query parameters and String validation](https://fastapi.tiangolo.com/tutorial/body/)

### Points

```python
  q: Optional[str] = Query(None, max_length=50, )
```

is equal to

```python
  q: Optional[str] = None
```

but without query conditions

* use default variable
* use regex
* set max and min length ` Query(...,max_length=50, min_length=5)`
* use alias `Query(None, alias="item-query")`
* use list as parameter `q: Optional[List[str]] = Query(None)`
* wanna use required? remove `Optional`!

## Path Parameters and Numeric Validations

## Order the parameters as you need, tricks

pass `*` as `kwargs`, it accepts all available variables

## Number validations: greater than or equal

* `gt`: Greater than
* `lt`: Less than
* `ge`: Greater than or Equal
* `le`: Less than or Equal

## Body - Multiple Parameters

### Mix Path, Query and body parameters

you can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.

```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

```

json body:

```json
{
  "item": {
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
  },
  "user": {
    "username": "dave",
    "full_name": "Dave Grohl"
  }
}

```

### Singular value in Body

marked it in function with `Body(...)`

```python
@app.put("/items/{item_id}")
async def update_item(
        item_id: int, item: Item, user: User, importance: int = Body(...)
):
    pass
```

### Declare Query Params

```python
@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(..., gt=0),
        q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
```

### Use a Parameter as Embded

```python
item: Item = Body(..., embed=True)
```

## Body - Fields
The same way you can declare additional validation and metadata in path operation function parameters with `Query`, `Path` and `Body`, you can declare validation and metadata inside of Pydantic models using Pydantic's `Field`.


## Security

### OAuth2 
OAuth2 is a specification that defines several ways to handle authentication and authorization.

It is quite an extensive specification and covers several complex use cases.

It includes ways to authenticate using a "third party".

That's what all the systems with "login with Facebook, Google, Twitter, GitHub" use underneath.


