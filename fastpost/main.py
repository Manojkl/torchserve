# from typing import Union

# from fastapi import FastAPI

# # import os
# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from pydantic import BaseSettings
# from pydantic import BaseSettings, Field

# SQLALCHEMY_DATABASE_URL = "postgresql://welcome:welcome@postgresql-service:5432/my_database"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()