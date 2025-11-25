from sqlalchemy.engine import Engine
from sqlmodel import Session, select
from modules.tables import *
from sqlalchemy.exc import NoResultFound


def find_agent(engine: Engine, agent_id: int):
    with Session(engine) as session:
        statement = select(Agent).where(Agent.id == agent_id)
        try:
            agent = session.exec(statement).one()
            return agent
        except NoResultFound:
            print(f"No agent found with id {agent_id}")
            return None

def create_agent(agent_name: str,agent_rank: str, password: str, engine: Engine):
    try: 
        with Session(engine) as session:
            agent = Agent(name=agent_name, password=password, rank=agent_rank)
            session.add(agent)
            session.flush()
            session.expunge(agent)
            session.commit()
        print("You have successfully registered")
        return agent
    except ValueError as e:
        return e

def create_tables(engine: Engine):
    SQLModel.metadata.create_all(engine)

def run_SQL_queries_freely(engine: Engine):
    pass

def create_an_intelligence_report(engine: Engine,  agent: Agent):
    terrorists = input("type the all terrorists by ,")
    data = input("type the report")
    report_id = create_new_report(engine, data, agent.id)
    create_new_terrorist(engine, terrorists, report_id)
    
def create_new_report(engine: Engine, data: str, agent_id: int):
    try: 
        with Session(engine) as session:
            report = Report(data=data, agentId=agent_id)
            session.add(report)
            session.flush()
            report_id = report.id
            session.commit()
        return report_id
    except ValueError as e:
        return e

def create_new_terrorist(engine: Engine, terrorists: str, report_id: int):
    
    names = [n.strip() for n in terrorists.split(",") if n.strip()]
    
    with Session(engine) as session:
        statement = select(Terrorist).where(Terrorist.name.in_(names))
        existing_terrorists = session.exec(statement).all()

        terrorists_by_name = {t.name: t for t in existing_terrorists}

        for name in names:
            terrorist = terrorists_by_name.get(name)
            
            if terrorist:
                terrorist.rank = (terrorist.rank or 0) + 1
                t_id = terrorist.id
            else:
                terrorist = Terrorist(name=name, rank=1)
                session.add(terrorist)
                session.flush()
                t_id = terrorist.id
                
            create_new_ReportHostileActor(session, t_id, report_id)

        session.commit()

def create_new_ReportHostileActor(session: Session, terrorists_id: int, report_id: int):
    try: 
        session.add(ReportHostileActor(reportId= report_id, terroristId= terrorists_id))
        session.flush()
        return "You have create report"
    except ValueError as e:
        return e
    
def delete_an_intelligence_report(engine: Engine, report_id: int):
    with Session(engine) as session:
        statement = select(Report).where(Report.id == report_id)
        if report := session.exec(statement).first():
            session.delete(report)
            session.commit()
        else:
            print("report not found")   

def search_reports_by_keywords(engine: Engine, keywords: str):
    with Session(engine) as session:
        statement = select(Report).where(Report.data.like(f"%{keywords}%"))
        print(session.exec(statement).all())

def search_reports_by_hostile_actor(engine: Engine, hostile_actor: str):
    with Session(engine) as session:
        statement = (
            select(Report)
            .join(ReportHostileActor, ReportHostileActor.reportId == Report.id)
            .join(Terrorist, ReportHostileActor.terroristId == Terrorist.id)
            .where(Terrorist.name.like(f"%{hostile_actor}%"))
        )
        reports = session.exec(statement).all()
        for report in reports:
            print(report)

def search_for_dangerous_hostile_actors(engine: Engine):
    print(search_for_dangerous(engine, 5))

def search_for_highly_dangerous_hostile_actors(engine: Engine):
    print(search_for_dangerous(engine, 10))
    
def search_for_dangerous(engine: Engine, num_rank: int):
    with Session(engine) as session:
        statement = select(Terrorist).where(Terrorist.rank >= num_rank)
        return session.exec(statement).all()

