#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa:"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City, State

if __name__ == '__main__':
    URL = 'mysql+mysqldb://{}:{}@localhost/{}'
    s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(URL.format(s1, s2, s3), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id):
        state = session.query(State).get(city.state_id).name
        print("{}: ({}) {}".format(state, city.id, city.name))
