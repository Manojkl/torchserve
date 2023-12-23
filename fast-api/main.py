# main.py

from fastapi import FastAPI

app = FastAPI()

# import os
from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings
from pydantic import BaseSettings, Field

SQLALCHEMY_DATABASE_URL = "postgresql://welcome:welcome@postgresql-service:5432/my_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@app.get("/")
async def root():
    return {"message": "Hello World, what's up"}


# from typing import Union

# from fastapi import FastAPI

# import os
# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from pydantic import BaseSettings
# from pydantic import BaseSettings, Field

# # import os

# app = FastAPI()

# SQLALCHEMY_DATABASE_URL = "postgresql://welcome:welcome@localhost:5432/my_database"


# SQLALCHEMY_DATABASE_URL
# DATABASE_URL = os.getenv("DATABASE_URL")
# class Settings(BaseSettings):
#     db_url: str = Field(..., env="DATABASE_URL")

# engine = create_engine(os.environ["DATABASE_URL"])
# settings = Settings()
# DATABASE_URL = settings.db_url
# DATABASE_URL = os.environ["DATABASE_URL"]
# engine = create_engine(DATABASE_URL)

# # engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    key = Column(String)
    value = Column(String)


Base.metadata.create_all(bind=engine)


@app.post("/store_data/")
async def store_data(user_id: int, key: str, value: str):
    db = SessionLocal()
    db_data = User(user_id=user_id, key=key, value=value)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return {"key": db_data.key, "value": db_data.value}


@app.get("/get_data/")
async def get_data(user_id: int, key: str):
    db = SessionLocal()
    data = db.query(User).filter(User.user_id == user_id, User.key == key).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"key": data.key, "value": data.value}


@app.delete("/delete_data/")
async def delete_data(user_id: int, key: str):
    db = SessionLocal()
    db_data = db.query(User).filter(User.user_id == user_id, User.key == key).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(db_data)
    db.commit()
    return {"message": "Data deleted successfully"}


@app.put("/increment/")
async def increment(user_id: int, key: str, x: int):
    db = SessionLocal()
    db_data = db.query(User).filter(User.user_id == user_id, User.key == key).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db_data.value = str(int(db_data.value) + x)
    db.commit()
    return {"message": f"Incremented by {x}"}


@app.put("/decrement/")
async def decrement(user_id: int, key: str, x: int):
    db = SessionLocal()
    db_data = db.query(User).filter(User.user_id == user_id, User.key == key).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db_data.value = str(int(db_data.value) - x)
    db.commit()
    return {"message": f"Decremented by {x}"}


@app.put("/getuser/")
async def getuser():
    db = SessionLocal()
    db_data = db.query(User).filter(User.user_id == user_id, User.key == key).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db_data.value = str(int(db_data.value) - x)
    db.commit()
    return {"message": f"Decremented by {x}"}


from typing import List


@app.get("/get_all_users/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()
