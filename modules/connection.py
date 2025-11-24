from sqlmodel import Field, Session, SQLModel, create_engine
from config import URL
from tables import * 


engine = create_engine(URL)


