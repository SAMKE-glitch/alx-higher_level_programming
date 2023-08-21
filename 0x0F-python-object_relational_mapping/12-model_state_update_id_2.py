#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a state object on the database
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    change_state = session.query(State).filter(State.id == '2').first()
    change_state.name = 'New Mexico'
    session.commit()
    session.close()
