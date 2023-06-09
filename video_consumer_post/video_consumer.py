from kafka import KafkaConsumer
import json
from db_connection import Session
from models import Video, Category

TOPIC_POST_VIDEO = "video-post-event"

def post_video(user_id, title, resume=None, category=None, category_id=None):
        with Session() as session:
            try: 
                video = Video(user_id=user_id, title=title, resume=resume,  category_id=category_id, category=category)
                session.add(video)
                session.commit()
                session.close()
                return None
            except Exception as e: 
                return str(e)
            finally:
                session.close()

def delete_video(id):
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

def add_like_video(id):
     with Session() as session:
            try: 
                session.query(Video).filter_by(video_id=id).update({'video_rating': Video.video_rating + 1})
                session.commit()
                return None
            except Exception as e: 
                return str(e)
            finally:
                session.close()


consumer = KafkaConsumer(
        bootstrap_servers=['kafka1:9092'],
        group_id='group1',
        value_deserializer=lambda v: json.loads(v.decode('ascii')),
        key_deserializer=lambda v: json.loads(v.decode('ascii')),
        max_poll_records=10,
        auto_offset_reset='earliest',
        session_timeout_ms=6000,
        heartbeat_interval_ms=3000
    )
consumer.subscribe(topics=[TOPIC_POST_VIDEO])



try:
    for message in consumer:
        print(message.key)
        post_video(
             user_id=message.value["user_id"], 
             title=message.value["title"], 
             resume=message.value["resume"], 
             category_id=message.value["category_id"], 
             category=message.value["category"]
             )
        

except Exception as e:
     print(str(e))