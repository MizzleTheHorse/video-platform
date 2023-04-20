from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import create_database, database_exists
from models import metadata

db_url_docker = "sqlite:///service/instance/video_database.sqlite"
db_url_local = f"sqlite:////home/emil/Desktop/Bachelor/system/video-platform/video/service/instance/video_database.sqlite"

mysql_ip = os.getenv("MYSQL_IP")

url = f"mysql+mysqldb://video_host:secret@{mysql_ip}:3307/video_database"


#if not database_exists(url):
##    print('no db found')
 #   create_database(url)
#    print('New database created')
try:
    engine = create_engine(url, pool_size=5, pool_recycle=3600)

    metadata.create_all(bind=engine)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
except Exception as e:
    print('Database not ready...')
