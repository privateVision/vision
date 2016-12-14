# -*- coding: utf-8 -*-
from contextlib import contextmanager
from sqlalchemy import create_engine

from vision.model.vision.base import BaseModel as vision_Model
from vision.model.vision.base import Session
from settings import sqlalchemy_db

def init_db():
    engine = create_engine(sqlalchemy_db, pool_recycle=3600)
    Session.configure(bind=engine)

    vision_Model.metadata.bind = engine
    vision_Model.metadata.create_all(checkfirst=True)

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