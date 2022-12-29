from fastapi import FastAPI
from fastapi import Depends
from fastapi import Body

from sqlalchemy.orm import Session

from database import SessionLocal
from database import engine

from models import User 
from models import Item

from serializers import item_serializer
from serializers import user_serializer

from typing import Dict 
from typing import Union

from schemas import UserSchema
from schemas import ItemSchema

app = FastAPI()

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
# This function is used by path operation functions to start db connection
# and close it at the end of its use.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user_serializer.dump(user)

@app.get('/items/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    return item_serializer.dump(item)

@app.post('/users/')
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_db = user_serializer.load(user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@app.post('/items/')
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    item_db = item_serializer.load(item.dict())
    db.add(item_db)
    db.commit()
    db.refresh(item_db)
    return item_db
