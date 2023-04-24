from kafka import KafkaConsumer
import json
from db_connection import Session
from models import Video, Category

TOPIC_POST_VIDEO = "video-post-event"

def post_video(user_id, title, resume=None, category_id=None):
        with Session() as session:
            try: 
                video = Video(user_id=user_id, title=title, resume=resume, category_id=category_id)
                session.add(video)
                session.commit()
                video = self.get_video(id=video.video_id)
                session.close()
                return video
            except Exception as e: 
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
        print(message.value["user_id"])
        print(message.value["title"])
        print(message.value["resume"])
        print(message.value["category_id"])
        post_video(user_id=message.value["user_id"], title=message.value["title"], resume=message.value["resume"], category_id=message.value["category_id"])
except Exception as e:
     print(str(e))