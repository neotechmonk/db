from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    ssn = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    gender = Column(CHAR)

    def __init__(self, ssn,firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Person(ssn='{self.ssn}', firstname='{self.firstname}', lastname='{self.lastname}', gender='{self.gender}', age={self.age})"

class Thing(Base):
    __tablename__ = "things"

    tid = Column(Integer, primary_key=True,autoincrement=True)
    description = Column(String)
    owner = Column(Integer, ForeignKey("person.ssn"))

    def __init__(self, description, owner):
        self.description = description
        self.owner = owner
    def __repr__(self):
        return f"Thing(tid={self.tid}, description='{self.description}', owned by {self.owner})"