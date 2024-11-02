from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

# Создание движка
engine = create_engine(settings.DATABASE_URL_psycopg, echo=False, pool_size=5, max_overflow=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# # Проверка подключения
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT version();"))
#     print(f"{result.first()=}")