from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db


def init_db() -> None:
    from . import models  # noqa: F401  (registers the tables)
    Base.metadata.create_all(engine)