from dataclasses import dataclass
from enum import Enum

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
