# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()
metadata = Base.metadata

engine = create_engine('mysql://dcmx:dcmx@localhost/face_comment_nakamura?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()


class Photo(Base):
    __tablename__ = 'photo'
    __table_args__ = {"mysql_charset": "utf8",'mysql_engine':'InnoDB'}

    id             = Column(mysql.BIGINT, primary_key=True)
    talent_id      = Column(INT(11))
    img_name       = Column(VARCHAR(500))
    img_file       = Column(VARCHAR(500))
    datetime       = Column(DATETIME())
    comment_count  = Column(INT(11))
    other          = Column(VARCHAR(500))
    blog_entry_url = Column(VARCHAR(500))

    def __init__(self,lists):
        self.talent_id       = lists['talent_id']
        self.img_name        = lists['img_name']
        self.img_file        = lists['img_file']
        self.datetime        = lists['datetime']
        self.comment_count   = lists['comment_count']
        self.other           = lists['photo_other']
        self.blog_entry_url  = lists['blog_entry_url']



class Talent(Base):
    __tablename__ = 'talent'
    __table_args__ = {"mysql_charset": "utf8",'mysql_engine':'InnoDB'}

    id                 = Column(mysql.BIGINT, primary_key=True)
    name               = Column(VARCHAR(500))
    profile_img_file   = Column(VARCHAR(500))
    sex                = Column(INT(2))
    other              = Column(VARCHAR(500))

    def __init__(self,lists):
        self.name               = lists['name']
        self.profile_img_file   = lists['profile_img_file']
        self.sex                = lists['sex']
        self.other              = lists['talent_other']

