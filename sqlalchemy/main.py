from pprint import pprint

from database import Session
from models import Person


def add_persons(session):
    person1 = Person(123, "Mike", "John", "m", 23)
    person2 = Person(124,"Jane", "Doe", "f", 35)
    person3 = Person(1234,"Bob", "Smith", "m", 45)
    person4 = Person(2134,"Alice", "Jones", "f", 27)
    person5 = Person(3451,"Tom", "Brown", "m", 31)

    session.add_all([person1, person2, person3, person4, person5])
    session.commit()

def get_all_persons(session):
    results = session.query(Person).all()
    return results

if __name__ == "__main__":
    session = Session()
    add_persons(session)
    results = get_all_persons(session)
    pprint(results)
