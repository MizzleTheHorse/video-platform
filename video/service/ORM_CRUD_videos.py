from db_connection import Session
from models import Video, Category
from sqlite3 import OperationalError, IntegrityError
from sqlalchemy.exc import IntegrityError

class DatabaseInterface:
    def __init__(self):
        pass
    
    def get_video(self, video_id=None, user_id=None):
        with Session() as session:
            try:
                if id:
                    result = (session.query(Video).filter(Video.video_id == video_id).first())
                    if result:
                        video = Video(video_id=result.video_id, user_id=result.user_id, title=result.title, resume=result.resume, category_id=result.category_id, category=result.category)
                        return video
                    else: 
                        return 'not found'
                else:
                    result = (session.query(Video).filter(Video.title == user_id).first())
                    if result:
                        video = Video(video_id=result.video_id, user_id=result.user_id, title=result.title, resume=result.resume, category_id=result.category_id, category=result.category)
                        return video
                    else: 
                        return 'not found'
            except Exception as e: 
                return str(e)
            finally:
                session.close()

    def post_video(self, user_id, title, resume=None, category_id=None, category=None):
        with Session() as session:
            try: 
                video = Video(user_id=user_id, title=title, resume=resume, category_id=category_id, category=category)
                session.add(video)
                session.commit()
                video = self.get_video(id=video.video_id)
                return video
            except Exception as e: 
                session.expunge_all()
                return str(e)
            finally:
                session.close()
            
    
    def delete_video(self, id):
        with Session() as session:
            try: 
                video = (session.query(Video).filter(Video.video_id == id).first())
                if video:
                    session.delete(video)
                    session.commit()
                    return video
                else: 
                    return 'not found'
            except Exception as e: 
                return str(e)
            finally:
                session.close()
            


    #Returns last 10 videos
    def get_latest_videos(self):
        with Session() as session:
            try: 
                result = (session.query(Video).limit(10).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))

    #Returns last 5 videos
    def get_latest_videos_user(self, id):
        with Session() as session:
            try: 
                result = (session.query(Video).filter(Video.user_id == id).limit(10).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))

    
    #Returns last 10 videos of a particular catoergy 
    def get_latest_videos_category(self, category_id):
        with Session() as session:
            try: 
                result = (session.query(Video).filter(Video.category_id == category_id).limit(10).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))

    def get_categories(self):
        with Session() as session:
            try: 
                result = (session.query(Category).all())
                return result
            except OperationalError as e:
                print('an error occured' + str(e))

    
    
    

# Create:
#video = Video(video_id=10, name='test_name', email='test_mail', hashed_password='$½¡@£#¤øæåÅØÆEOL')
