from typing import Optional

from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Baz"},
                 {"item_name": "Baz"}, {"item_name": "Baz"}, {"item_name": "Baz"}, {"item_name": "Baz"},
                 {"item_name": "Baz"}, {"item_name": "Baz"}, {"item_name": "Baz"}, {"item_name": "Baz"},
                 {"item_name": "Baz"}, {"item_name": "Baz"}, {"item_name": "Baz"}, ]

app = FastAPI()


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/foo/{item_id}")
async def read_item_by_id(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/desc/{item_id}")
async def desc(item_id: str, q: Optional[str] = None, short: bool = False):
    response = {"item_id": item_id}
    if q:
        response.update({"q": q})
    if not short:
        response.update({"description": "This is an amazing item that has a long description"})
    return response


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    response = {"item_id": item_id, "owner_id": user_id}
    if q:
        response.update({"q": q})
    if not short:
        response.update({"description": "This is an amazing item that has a long description"})
    return response


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
