from sqlmodel import Field, Session, SQLModel, create_engine
from config.config import URL
from modules.tables import * 

def get_angine():
    engine = create_engine(URL)
    return engine


