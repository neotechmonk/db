from sqlalchemy import CHAR, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    age = Column("age", Integer)
    gender = Column("gender", CHAR)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Person(firstname='{self.firstname}', lastname='{self.lastname}', gender='{self.gender}', age={self.age})"


engine = create_engine("sqlite:///person_db.db", echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
person = Person(123, "Mike", "John", "m", 23)
session.add(person)
session.commit()
person1 = Person(123456789, "Mike", "John", "m", 23)
person2 = Person(987654321, "Jane", "Doe", "f", 35)
person3 = Person(555555555, "Bob", "Smith", "m", 45)
person4 = Person(111111111, "Alice", "Jones", "f", 27)
person5 = Person(222222222, "Tom", "Brown", "m", 31)

session.add_all([person1, person2, person3, person4, person5])
session.commit()
