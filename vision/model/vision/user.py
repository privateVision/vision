# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, text, Sequence, Index
from utils.database import BaseModel

class User(BaseModel):
    __tablename__ = 'user'
    user_id = Column(Integer, Sequence('tb_user_id_seq', metadata=BaseModel.metadata, start=1000), primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(255), nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=text("now()"))
    update_at = Column(DateTime, nullable=False, server_default=text("now()"))

    __table_args__ = (
        Index('user_email_uindex', email, unique=True),
        Index('user_index', user_id, unique=True),
    )

class UserInfo(BaseModel):
    __tablename__ = 'user_info'
    user_id = Column(Integer, Sequence('tb_user_info_id_seq', metadata=BaseModel.metadata, start=100000), primary_key=True)


