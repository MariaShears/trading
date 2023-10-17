from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import c as config

_engine = create_engine(f"sqlite:///{config.db_name}")
_Session = sessionmaker(bind=_engine)
session = _Session()
Base = declarative_base()
