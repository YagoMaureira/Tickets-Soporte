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


Base.metadata.create_all(bind=engine)
