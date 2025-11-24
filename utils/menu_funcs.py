from utils.io import *
from querys import *
def check_connected_agent() -> int | None:
    with open(r"logged_agent/logged.txt",'r+') as file:
        content = file.read()
        if content:
            agent_id = content
            return agent_id
        else:
            return None

def create_new_agent():
    agent_name = input("enter agent name:\n")
    agent_rank = input("enter agent rank:\n")
    create_agent(agent_name,agent_rank)



def agent_connection(engine):
    while True:
        agent_name = input("enter agent name:\n").strip().lower()
        agent_password = input("enter password:\n")

        if agent := find_agent(engine,agent_name):
            if agent.password == agent_password:
                return agent.id
            else:
                print("incorrect password")
                continue
         
def get_connected_agent(engine):
    if agent_id := check_connected_agent():
        agent = find_agent(engine,agent_id)
        return agent 
    else:
        print("There is no agent saved in the system.")
        return None

def connect(engine):
    while True:
        user_choice = input(connection_menu)
        match user_choice:
            case '1':
                return create_new_agent(engine)
            case '2':
                return agent_connection(engine)
            case '3':
                agent = get_connected_agent(engine)
                if agent:
                    return agent
            case _:
                print("invalid input")    
            
def log_out():
    with open(r"logged_agent/logged.txt",'w') as file:
        file.write("")


def write_agent_as_connected(agent):
     with open(r"logged_agent/logged.txt",'w') as file:
        file.write(agent.id)