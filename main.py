from queries import *
from utils.menu_funcs import *
from utils.io import * 
from db.connection import get_engine



admin_password = '123'

engine = get_engine()


create_tables(engine)

while True:
    agent = connect(engine)

    if not agent:
        break

    write_agent_as_connected(agent)
    while True:
        agent_choice = input(menu_message)

        match agent_choice:
            case '1':
                password = in_pass()
                if password == admin_password:
                    run_SQL_queries_freely(engine)
                else:
                    print("invalid password")
            case '2':
                create_an_intelligence_report(engine,agent)
            case '3':
                report_id = in_report_id()
                delete_an_intelligence_report(engine,report_id)
            case '4':
                keywords = in_search_keywords()
                search_reports_by_keywords(engine,keywords)
            case '5':
                hostile_actor = in_search_hostile_by_actor()
                search_reports_by_hostile_actor(engine,hostile_actor)
            case '6':
                search_for_dangerous_hostile_actors(engine)
            case '7':
                search_for_highly_dangerous_hostile_actors(engine)
            case '8':
                log_out()
                break
            case '0':
                break
            case _:
                print("invalid input")

