from typing import Union
from fastapi import FastAPI 

from models import Student
from models import School
from models import ModelName

app = FastAPI()

@app.get("/")
def read_item():
    return {'Hello': 'world'}


@app.get('/item/{item_id}')
def get_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

@app.get('/models/{model_name}')
def get_model(model_name: ModelName):
    
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'id': 1}
    
    if model_name == ModelName.resnet.value:
        return {'model_name': model_name, 'id': 2}

    return {'model_name': model_name, 'id': 3}