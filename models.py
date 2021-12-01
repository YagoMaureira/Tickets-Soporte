from sqlalchemy import String, Integer, Column, DateTime, MetaData, Date
from db_config import Base, engine


class Ticket(Base):

    __tablename__ = "tickets"
    ticket_id = Column(Integer, primary_key=True)
    title = Column(String(45), nullable=False)
    author = Column(String(45), nullable=False)
    description = Column(String(200), nullable=False)
    status = Column(String(45), nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self, title, author, description, status, date):

        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date

    def to_json(self):
        ticket_json = {
            'ticket_id': self.ticket_id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'status': self.status,
            'date': str(self.date)
        }
        return ticket_json


Base.metadata.create_all(bind=engine)
