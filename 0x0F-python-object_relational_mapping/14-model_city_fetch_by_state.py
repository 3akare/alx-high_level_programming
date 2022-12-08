#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import model_city

if __name__ == '__main__':
    URL = 'mysql+mysqldb://{}:{}@localhost/{}'
    s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(URL.format(s1, s2, s3), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    