from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASS')}@localhost/{getenv('DB_NAME')}")

Session = sessionmaker(bind=engine)
sessionobj = Session()

Base = declarative_base(bind=engine)
