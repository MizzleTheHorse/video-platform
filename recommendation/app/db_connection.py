from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from .models import metadata

mysql_ip = os.getenv("MYSQL_IP")

url = f"mysql+mysqldb://recommendation_host:secret@{mysql_ip}:3308/recommendation_database"

try:
    engine = create_engine(url, pool_size=5, pool_recycle=3600)

    metadata.create_all(bind=engine)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
except Exception as e:
    print(e)    
    print('Database not ready...')
