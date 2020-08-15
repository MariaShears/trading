from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import c as config

_engine = create_engine(f"sqlite:///{config.db_name}", echo=True)
_Session = sessionmaker(bind=_engine)
session = _Session()
Base = declarative_base()