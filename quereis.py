from sqlalchemy.engine import Engine
from sqlmodel import Session, select
from modules.tables import *


def find_agent(engine,agent_id):
      with Session as session:
        statement = select(Agent).where(agent_id.id == agent_id)
        if agent := session.exec(statement).one():
            return agent
        else:
            return None

def create_agent(agent_name: str,agent_rank: str, password: str, engine: Engine):
    try: 
        with Session(engine) as session:
            session.add(Agent(agent_name, password, agent_rank))
            session.commit()
        return "You have successfully registered"
    except ValueError as e:
        return e

def create_tables(engine: Engine):
    SQLModel.metadata.create_all(engine)

def run_SQL_queries_freely(engine: Engine):
    pass

def create_an_intelligence_report(engine: Engine,  agent: Agent):
    try: 
        terrorists = input("type the all terrorists by ,")
        data = input("type the report")
        with Session(engine) as session:
            session.add(Report(data, agent.id))
            session.commit()
        create_new_terrorist(engine, terrorists)
        return "You have create report"
    except ValueError as e:
        return e
    
def create_new_terrorist(engine: Engine, terrorists: str):
    try: 
        with Session(engine) as session:
            for t in terrorists.split(','):
                statement = select(Terrorist).where(Terrorist.name == t)
                if ter:= session.get(statement):
                    ter.ra
                session.commit()
        return "You have successfully create terrorist"
    except ValueError as e:
        return e

def create_new_ReportHostileActor(engine: Engine, terrorists_id: id, report_id: int):
    try: 
        with Session(engine) as session:
            session.add(ReportHostileActor(report_id, terrorists_id))
            session.commit()
        return "You have create report"
    except ValueError as e:
        return e
    
def delete_an_intelligence_report(engine: Engine, report_id: int):
    with Session as session:
        statement = select(Report).where(Report.id == report_id)
        if report := session.exec(statement).one():
            session.delete(report)
            session.commit()
        else:
            print("report not found")   

def search_reports_by_keywords(engine: Engine, keywords: str):
    with Session(engine) as session:
        statement = select(Report).where(Report.data.like == f"%{keywords}%" )
        return session.exec(statement).all()

def search_reports_by_hostile_actor(engine: Engine,hostile_actor: str):
    with Session(engine) as session:
        statement = select(ReportHostileActor , Terrorist).join(Terrorist).where(Terrorist.name.like == f"%{hostile_actor}%")
        reports = session.exec(statement).all()
        print(reports)

def search_for_dangerous_hostile_actors(engine: Engine):
    print(search_for_dangerous(engine, 5))

def search_for_highly_dangerous_hostile_actors(engine: Engine):
    print(search_for_dangerous(engine, 10))
    
def search_for_dangerous(engine: Engine, num_rank: int):
    with Session(engine) as session:
        statement = select(Terrorist).where(Terrorist.rank >= num_rank)
        return session.exec(statement).all()

