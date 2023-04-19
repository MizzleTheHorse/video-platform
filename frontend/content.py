from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask, request, render_template, Response, stream_with_context
from flask import current_app as app
from flask_login import current_user
from .models import Video
from kafka import KafkaConsumer, KafkaProducer
import json
from .video_client import VideoClient


content = Blueprint('content', __name__)
client = VideoClient()

TOPIC_POST_VIDEO = "video-post-event"
TOPIC_POST_WATCHED = "video-post-watch-event"

category_list = ['Sports' , 'Outdoor', 'Music', 'Gaming', 'DIY', 'Food', 'Programming', 'Animals', 'Education']

video_dic = {
  "1": "After returning from their honeymoon and showing home movies to their friends, Shrek and Fiona learn that her parents have heard that she has married her true love and wish to invite him to their kingdom, called Far Far Away. The catch is: Fiona's parents are unaware of the curse that struck their daughter and have assumed she married Prince Charming, not a 700-pound ogre with horrible hygiene and a talking donkey pal.",
  "2": "Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, and thanks to his supportive mother (Sally Field), he leads anything but a restricted life. Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares about most may be the most difficult to save -- his childhood love, the sweet but troubled Jenny (Robin Wright).",
  "3": "This sweeping drama, based on real historical events, follows American boyhood friends Rafe McCawley (Ben Affleck) and Danny Walker (Josh Hartnett) as they enter World War II as pilots. Rafe is so eager to take part in the war that he departs to fight in Europe alongside England's Royal Air Force. On the home front, his girlfriend, Evelyn (Kate Beckinsale), finds comfort in the arms of Danny. The three of them reunite in Hawaii just before the Japanese attack on Pearl Harbor.",
  "test": "test test test ", 
  "test2": "test test test ", 
  "test3": "test test test ", 
  "test4": "test test test ", 
  "test5": "test test test ", 
  "test6": "test test test ", 
  "test7": "test test test ", 
}



def stream_template(template_name, **context):
    """Enabling streaming back results to template"""
    app.update_template_context(context)
    template = app.jinja_env.get_template(template_name)
    streaming = template.stream(context)
    #streaming = template.stream_with_context(context)
    return streaming


@content.route('/latest')
def latest():
    content = client.get_latest_videos()
    print(type(content))
    print(content)
    return render_template('latest.html', content=video_dic)


@content.route('/category')
def category():
    return render_template('category.html', categories=category_list)


@content.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        try:
            producer = KafkaProducer(
            bootstrap_servers='kafka1:9092', 
            value_serializer=lambda v: json.dumps(v).encode('ascii'),
            key_serializer=lambda v: json.dumps(v).encode('ascii'))
            producer.send(
            TOPIC_POST_VIDEO,
            key={"video_id": 'test123'},
            value={
                "user_id": 1,
                "title": request.form.get("title"),
                "resume": request.form.get("resume"),
                "category": request.form.get("category")
            })
            producer.flush()
            flash('Uploaded video, check /view to see.')
            return redirect(url_for('content.video')) # if user doesn't exist or password is wrong, reload the page
        except Exception as e: 
            flash('No brokers are available, try again later. Error: ' + str(e))
            return redirect(url_for('content.video')) # if user doesn't exist or password is wrong, reload the page

    else:
        return render_template('upload.html')

@content.route('/video/<int:video_id>', methods=['GET'])
def test():
    pass


@content.route('/view')
def view():
    try:
        consumer = KafkaConsumer(
            bootstrap_servers=['kafka1:9092'], 
            group_id='group1',
            value_deserializer=lambda v: json.loads(v.decode('ascii')),
            key_deserializer=lambda v: json.loads(v.decode('ascii')),
            max_poll_records=5,
            auto_offset_reset='latest',
            session_timeout_ms=6000,
            heartbeat_interval_ms=3000
        )
        consumer.subscribe(topics=[TOPIC_POST_VIDEO])
        
        def consume_msg():
            for message in consumer:
                print('RECIEVED CONSUMER DATA')
                print(message.value)
                yield [
                    message.value["user_id"],
                    message.value["title"],
                    message.value["resume"],
                    message.value["category"]]
    except Exception as e:
        flash('No brokers are available, try again later. Error: ' + str(e))
        return redirect(url_for('content.video')) # if user doesn't exist or password is wrong, reload the page
    return Response(stream_with_context(stream_template('video.html', data=consume_msg())))



@content.route('/watch-video/<int:id>', methods=['POST'])
def video_watched_event(id):
    producer = KafkaProducer(
    bootstrap_servers='kafka1:9092', 
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii'))
    producer.send(
    TOPIC_POST_VIDEO,
    key={"video_id": 'test123'},
    value={
        "user_id": 1,
        "title": request.form.get("title"),
        "resume": request.form.get("resume"),
        "category": request.form.get("category")
    })
    producer.flush()
    return 'Video successfully watched'

  