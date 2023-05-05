from models import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///person_db.db", echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
