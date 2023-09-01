import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, primary_key=True)
    Nick = Column(String(30), nullable=False, unique=True)
    Password = Column(String(20), nullable=False)
    Date = Column(Date, nullable=True)
    email = Column(String(40), nullable=False, unique=True)
    StatusID = Column(Integer, relationship(Status))

class Status(Base):
    __tablename__ = 'status'
    StatusID = Column(Integer, ForeignKey('user.StatusID'), primary_key=True)
    Status = Column(String(15), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    CommentID = Column(Integer, primary_key=True)
    Comment_text = Column(String(250), nullable=False)
    UserID = Column(Integer, ForeignKey(user.UserID))






# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
