from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists
from models import metadata

db_url_docker = "sqlite:///service/instance/video_database.sqlite"

db_url_local = "sqlite:////home/emil/Desktop/Bachelor/system/video-platform/video/service/instance/video_database.sqlite"

url = 'mysql+mysqldb://video_host:secret@172.21.0.2:3307/video_database'



if not database_exists(url):
    print('no db found')
    create_database(url)
    print('New database created')

engine = create_engine(url, pool_size=5, pool_recycle=3600)

metadata.create_all(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)