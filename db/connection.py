from sqlmodel import Field, Session, SQLModel, create_engine
from db.config import URL
from modules.tables import * 

def get_engine():
    return create_engine(URL)
   


