from fastapi import (
    APIRouter,
    Depends,
    status,
)
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
route = APIRouter(prefix="/todo", tags=["Todo"])
    

@route.get("/")
def get_all():
    return {"Hello": "Todo"}


@route.get("/items/")
def read_items():
    return [{"name": "Foo", "price": 42}, {"name": "Bar", "price": 42}]


@route.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
  
  
@route.post("/items/")
def create_item(item: Item):
    return item
  

@route.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
  

@route.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id}
  

