open_message = """Welcome to a terminal-based application
that enables an intelligence agent to connect to the system
and enter, update, or search intelligence reports on hostile actors,
using a database powered by an ORM (SQLModel)."""

menu_message = """
● Run SQL queries freely (developer/administrator mode) 1
● Create an intelligence report                         2
● Delete an intelligence report                         3
● Search reports by keywords                            4
● Search reports by hostile actor                       5
● Search for dangerous hostile actors                   6
● Search for highly dangerous hostile actors            7
● log out                                               8
● Exit the system                                       9
"""

def check_connected_agent() -> int | None:
    with open(r"logged_agent/logged.txt",'r+') as file:
        content = file.read()
        if content:
            agent_id = content
            return agent_id
        else:
            return None

def agent_connection():
    while True:
        agent_name = input("enter agent name:\n").strip().lower()
        agent_password = input("enter password:\n")

        if agent := find_agent(agent_name):
            if agent.password == agent_password:
                return agent_id
            else:
                print("incorrect password")
                continue
        user_choice = input("the agent name is not in the system\n wold you like to creat a new one?\n") 

def get_connected_agent():
    if check_connected_agent():
        return check_connected_agent() 
    else:
        return agent_connection()


while True:
    connected_agent = get_connected_agent()
    if not connected_agent:
        continue
    agent_choice = input(menu_message)
    match agent_choice:
        case '1':
            run_SQL_queries_freely()
        case '2':
            create_an_intelligence_report()
        case '3':
            delete_an_intelligence_report()
        case '4':
            search_reports_by_keywords() 
        case '5':
            search_eports_by_keywords()
        case '6':
            search_for_dangerous_hostile_actors()
        case '7':
            search_for_highly_dangerous_hostile_actors()
        case '8':
            log_out()
        case '9':
            break
        case _:
            print("invalid input")



