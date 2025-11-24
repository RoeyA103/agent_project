from sqlalchemy.engine import Engine
from sqlmodel import Session, select
from modules.tables import *
from db.connection import engine



def create_tables(engine: Engine):
    SQLModel.metadata.create_all(engine)

def run_SQL_queries_freely(engine: Engine):
    pass
def create_an_intelligence_report(engine: Engine):
    pass
def delete_an_intelligence_report(engine: Engine):
    pass
def search_reports_by_keywords(engine: Engine, keywords: str):
    with Session(engine) as session:
        statement = select(Report).where(Report.data.like == f"%{keywords}" )
        return session.exec(statement).all()

def search_for_dangerous_hostile_actors(engine: Engine):
    return search_for_dangerous(engine, 5)

def search_for_highly_dangerous_hostile_actors(engine: Engine):
    return search_for_dangerous(engine, 10)
    
def search_for_dangerous(engine: Engine, num_rank: int):
    with Session(engine) as session:
        statement = select(Terrorist).where(Terrorist.rank >= num_rank)
        return session.exec(statement).all()

def log_out(engine: Engine):
    pass

search_reports_by_keywords(engine)
# create_tables(engine)