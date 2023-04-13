from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists
from models import metadata

db_url = "sqlite:///service/instance/user_database.sqlite"

if not database_exists(db_url):
    print('no db found')
    create_database(db_url)
    print('New database created')

engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

metadata.create_all(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
