import db

from db import session_scope
from db.models import Entry

def insert(entry):
    with session_scope() as session:
        session.add(entry)
        session.commit()


def retrieve():
    instances = []
    with session_scope() as session:
        for instance in session.query(Entry).order_by(Entry.id): 
            print instance
            instances.append(str(instance))
    return instances

