from database import Session
from models import Person

session = Session()

person1 = Person("Mike", "John", "m", 23)
person2 = Person("Jane", "Doe", "f", 35)
person3 = Person("Bob", "Smith", "m", 45)
person4 = Person("Alice", "Jones", "f", 27)
person5 = Person("Tom", "Brown", "m", 31)

session.add_all([person1, person2, person3, person4, person5])
session.commit()
