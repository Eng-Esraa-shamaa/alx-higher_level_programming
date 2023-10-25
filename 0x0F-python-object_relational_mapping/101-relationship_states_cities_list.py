#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]
                                    ),
                            pool_pre_ping=True
                          )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    qu = session.query(State).all()
    for x in qu:
        print("{}: {}".format(x.id, x.name))
        for i in x.cities:
            print("    {}: {}".format(i.id, i.name))
    session.close()
