from sqlmodel import Field, Session, SQLModel, create_engine
from db.config import URL
from modules.tables import * 


engine = create_engine(URL)


