from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists
from models import metadata
import pymysql

db_url_test = "sqlite:///service/instance/user_database.sqlite"

db_url  = 'mysql+mysqldb://root:root@127.0.0.1/user_database'

url = 'mysql+mysqldb://user_host:secret@192.168.87.175/user_database'


#
#if not database_exists(db_url):
#    print('no db found')
#    create_database(db_url)
#    print('New database created')

engine = create_engine(url, pool_size=5, pool_recycle=3600)

metadata.create_all(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
