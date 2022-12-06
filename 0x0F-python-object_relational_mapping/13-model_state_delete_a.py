#!/usr/bin/python3
"""Deletes every state with a name that contains the letter 'a'
from a database using SQLAlchemy with certain database configuration
specified via cmdline args.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    [db_username, db_password, db_name] = sys.argv[1:]

    connection_configuration = {
        'host': 'localhost',
        'user': db_username,
        'passwd': db_password,
        'db': db_name,
        'port': 3306
    }

    address = 'mysql://{user}:{passwd}@{host}:{port}/{db}'

    engine = create_engine(address.format(**connection_configuration))

    session_base_class = sessionmaker(engine)
    session = session_base_class()

    query = session.query(State)\
        .filter(State.name.contains('a'))\
        .delete(synchronize_session='fetch')

    session.commit()
