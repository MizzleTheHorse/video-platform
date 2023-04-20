from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists
from models import metadata
import os, time

#db_url_test = "sqlite:///service/instance/user_database.sqlite"

MYSQL_IP = os.getenv("MYSQL_IP")

url = f'mysql+mysqldb://recommedation_host:secret@{MYSQL_IP}/recommendation_database'


#
#if not database_exists(db_url):
#    print('no db found')
#    create_database(db_url)
#    print('New database created')
try:
    engine = create_engine(url, pool_size=5, pool_recycle=3600)

    metadata.create_all(bind=engine)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
except Exception as e:
    print('Database not ready...')
