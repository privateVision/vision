# -*- coding: utf-8 -*-
from contextlib import contextmanager
from sqlalchemy import create_engine

# from vision.model.vision.base import BaseModel as vision_Model
# from vision.model.vision.base import Session
from settings import sqlalchemy_db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

Session = sessionmaker()
session = Session()

class CRUDMixin():
    @classmethod
    def create(cls, commit=False, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save(commit=commit)

    def update(self, commit=False, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save(commit=commit) or self

    def save(self, commit=False):
        """Save the record."""
        session.add(self)
        if commit:
            session.commit()
        return self

    def delete(self, commit=False):
        """Remove the record from the database."""
        session.delete(self)
        return commit and session.commit()

class BaseModel(CRUDMixin, Base):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def init_db():
    engine = create_engine(sqlalchemy_db, pool_recycle=3600)
    Session.configure(bind=engine)

    BaseModel.metadata.bind = engine
    BaseModel.metadata.create_all(checkfirst=True)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()