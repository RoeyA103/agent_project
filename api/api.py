from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app("/create/{report}")
def create_an_intelligence_report(engine,agent):
    pass

@app("/search/")
    run_SQL_queries_freely(engine)


    create_an_intelligence_report(engine,agent)

  
    delete_an_intelligence_report(engine,report_id)

    search_reports_by_keywords(engine) 

 
    search_reports_by_hostile_actor(engine,hostile_actor)

    search_for_dangerous_hostile_actors(engine)

    search_for_highly_dangerous_hostile_actors(engine)

    log_out()

if __name__ == "__main__":
    uvicorn.run(
        "hero:app",
        host="localhost",
    port=8008,
        reload=True
    )