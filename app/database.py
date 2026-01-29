from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Defining DB Url
DATABASE_URL = "sqlite:///./food_delivery.db"

#Creating Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session connection to our Engine
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()    