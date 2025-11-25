from quereis import *
from utils.menu_funcs import *
from utils.io import *
from db.connection import connection



admin_password = '123'



while True:
    engine = connection.get_engine()

    agent = connect(engine)

    write_agent_as_connected(agent)

    agent_choice = input(menu_message)
    match agent_choice:
        case '1':
            password = input("enter admin password:\n")
            if password == admin_password:
                run_SQL_queries_freely(engine)
            else:
                print("invalid password")
        case '2':
            create_an_intelligence_report(engine,agent)
        case '3':
            delete_an_intelligence_report(engine)
        case '4':
            search_reports_by_keywords(engine) 
        case '5':
            search_reports_by_keywords(engine)
        case '6':
            search_for_dangerous_hostile_actors(engine)
        case '7':
            search_for_highly_dangerous_hostile_actors(engine)
        case '8':
            log_out()
        case '0':
            break
        case _:
            print("invalid input")



