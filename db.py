"""Database session factory"""
from fastapi_utils.session import FastAPISessionMaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

SessionMarkerFastAPI = FastAPISessionMaker(SQLALCHEMY_DATABASE_URL)


def get_db():
    """get_db - Database session factory."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
