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
● Exit the system                                       0
"""

connection_menu ="""
create new agent                     1
log in                               2
continue as the last connected agent 3
exit                                 0
"""


def in_pass():
    return input("enter admin password:\n")

def in_report_id():
    return int(input("enter report id:\n"))

def in_search_keywords():
    return input("enter keywords:\n")

def in_search_hostile_by_actor():
    return input("enter hostile actor name:\n")

def enter_terrorist():
    return input("Type all terrorists separated by commas:\n")