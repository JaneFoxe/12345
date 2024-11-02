import asyncio
import json

import aio_pika
from aio_pika import channel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import SessionLocal

# Создание приложения FastAPI
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


