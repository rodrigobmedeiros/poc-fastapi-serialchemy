from typing import Union
from typing import List
from typing import Dict

from fastapi import FastAPI 

from models import ModelName
from models import Item

app = FastAPI()

items: List[Item] = []
item = Item(name='potato', price=1)

items.append(item)

@app.get("/")
def read_item():
    return {'Hello': 'world'}

@app.get('/item/first')
def get_first_item(
    q: Union[str, None] = None
) -> Dict[str, Union[Item, str, None]]:

    item: Item = items[0]
    return {'item': item, 'q': q}

@app.get('/item/{item_id}')
def get_item(item_id: int, q: Union[str, None] = None) -> Item:
    return item
