from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.model import Base

DATABASE_URL = "sqlite:///notes.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

