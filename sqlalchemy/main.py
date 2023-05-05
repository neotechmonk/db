from pprint import pprint

from database import Session
from models import Person


def add_persons(session):
    person1 = Person(123, "Mike", "John", "m", 23)
    person2 = Person(124,"Jane", "Doe", "f", 35)
    person3 = Person(1234,"Bob", "Smith", "m", 45)
    person4 = Person(2134,"Alice", "Smith", "f", 27)
    person5 = Person(3451,"Tom", "Brown", "m", 31)

    session.add_all([person1, person2, person3, person4, person5])
    session.commit()

def get_all_persons(session):
    return session.query(Person).all()



def findby_name(session, search):
    """
        Eg.  Additional filtering options 
            Person.last_name.like(%'Smi'%) #similar to SQL like
            Person.first_name.in_(['Peter','Roudy'])
            Person.last_name.age > 34
    """
    return session.query(Person).filter(Person.lastname == search).all()


if __name__ == "__main__":
    session = Session()
    # add_persons(session)
    # pprint(get_all_persons(session))

    # Search people by the last name
    for x in findby_name(session, 'Smith'): 
        pprint(x)