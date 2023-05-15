from kafka import KafkaConsumer
import json
from db_connection import Session
from models import UserAction

TOPIC_RATE_WATCH = "video-rate-watch-event"

def post_user_action(action, user_id, video_id):
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
consumer.subscribe(topics=[TOPIC_RATE_WATCH])


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