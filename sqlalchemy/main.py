from pprint import pprint

from database import Session
from models import Person, Thing

from sqlalchemy import func


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

def give_thing_to_person(session: Session, person: Person, thing: str):
    return Thing( description = thing, owner=person)
if __name__ == "__main__":
    session = Session()
    #insert
    # add_persons(session)

    #Fetch all persons
    # pprint(get_all_persons(session))

    # Search people by  last name
    for x in findby_name(session, 'Smith'): 
        pprint(x)


    #lets gift
    surprise_gift ='Macbook Promax plus plus'
    rando = session.query(Person).order_by(func.random()).first()
    print(give_thing_to_person(session=session, person=rando, thing=surprise_gift))