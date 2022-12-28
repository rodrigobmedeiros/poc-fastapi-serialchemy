from typing import Union
from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel

@dataclass
class School:
    name: str

@dataclass
class Student:
    name: str
    age: int
    school: School

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Union[str, None]= None
    price: float
    tax: Union[float, None] = None
    