from .db_connection import Session
from .models import UserAction
from sqlite3 import OperationalError, IntegrityError

class DatabaseInterface:
    def __init__(self):
        pass
    
    #Returns last 5 videos
    def get_latest_user_actions(self, user_id):
        with Session() as session:
            try: 
                result = (session.query(UserAction).filter(UserAction.user_id == user_id).limit(5).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))
    

    #Returns last 5 videos
    def get_latest_user_actions_with_param(self, user_id, action):
        with Session() as session:
            try: 
                result = (session.query(UserAction).filter(UserAction.user_id == user_id, UserAction.action == action).limit(5).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))


# Create:
#video = Video(video_id=10, name='test_name', email='test_mail', hashed_password='$½¡@£#¤øæåÅØÆEOL')
