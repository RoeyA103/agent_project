from sqlmodel import Field, SQLModel
from datetime import datetime


class Agent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    password: str = Field(max_length=8)
    rank: str = Field(max_length=10)

class Terrorist(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    rank: str = Field(max_length=10)

class Report(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.now)
    agentId: int | None = Field(default=None, foreign_key="agent.id")
    
class TableToReports(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    reportId: int | None = Field(default=None, foreign_key="report.id")
    terroristId: int | None = Field(default=None, foreign_key="terrorist.id")
