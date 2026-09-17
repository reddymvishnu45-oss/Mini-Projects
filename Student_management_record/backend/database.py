import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:vishnuvardhan%40536@localhost:5432/project_db")
engine = create_engine(DATABASE_URL,pool_pre_ping = True)
SessionLocal = sessionmaker(bind=engine,autoflush=True,autocommit= False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()