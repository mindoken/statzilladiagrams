from flask_login import UserMixin
from flask_sqlalchemy import *
from flask_sqlalchemy.model import Model
from sqlalchemy import Column, Integer, String


class User(UserMixin, Model):
    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))