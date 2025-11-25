from sqlmodel import create_engine
from db.config import DB
from modules.tables import * 

def get_engine():
    return create_engine(DB)


