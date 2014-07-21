from db import Base#, ModelMixin

from sqlalchemy import Column, DateTime, Integer, String


class Entry(Base):#, ModelMixin):
    name = Column(String(100))
    subject = Column(String(100))
    homework = Column(String(100))  
    filename =  Column(String(100))  
    created = Column(DateTime)

    def __init__(self, name, subject, homework, filename, created):
        self.name = name
        self.subject = subject
        self.homework = homework
        self.filename =  filename 
        self.created = created

    def __repr__(self):
        return '<Entry({0} posted {1} {2} as {3} on {4})>'.format(
            self.name, self.subject, self.homework, self.filename, self.created)

    def __str__(self):
        return '{0} posted {1} {2} as {3} on {4}'.format(
            self.name, self.subject, self.homework, self.filename, self.created)


    