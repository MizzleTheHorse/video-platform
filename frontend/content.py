from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask, request, render_template, Response, stream_with_context
from flask import current_app as app
from flask_login import current_user, login_required 
#from .models import Video
from kafka import KafkaConsumer, KafkaProducer
import json
from .video_client import VideoClient
from .video_service_pb2 import Video


content = Blueprint('content', __name__)
client = VideoClient()

TOPIC_POST_VIDEO = "video-post-event"
TOPIC_DELETE_VIDEO = "video-post-event"

TOPIC_WATCHED_VIDEO = "video-watch-event"
TOPIC_RATE_VIDEO = "video-rate-event"


category_dict = {
    0 : 'Sports',
    1 : 'Outdoor',
    2 : 'Music',
    3 : 'Gaming',
    4 : 'DIY',
    5 : 'Food',
    6 : 'Programming',
    7 : 'Animals',
    8 : 'Education'
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
    video = client.get_latest_videos()
    video_list = []
    if not video:
        flash('No videos are available yet, be the first to upload!')
        return redirect(url_for('content.video'))
    for x in video.videos:
        video_list.append(x)
    video_list.reverse()
    return render_template('latest.html', content=video_list)


@content.route('/category')
def category():
    content = client.get_categories()
    return render_template('category.html', categories=content.categories)


@content.route('/category/<int:category_id>', methods=['GET'])
def category_video(category_id):
    content = client.get_latest_videos_category(category_id)
    category = category_dict[category_id]
    if not content:
        flash('No videos are available for this category')
        return redirect(url_for('content.category'))
    return render_template('category_videos.html', content=content.videos, category=category)



@content.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        try:
            if current_user.is_authenticated:
                user_id = current_user.user_id
            else:
                user_id = 0
            
            category_id = [k for k, v in category_dict.items() if v == request.form.get("category")]
            producer = KafkaProducer(
            bootstrap_servers='kafka1:9092', 
            value_serializer=lambda v: json.dumps(v).encode('ascii'),
            key_serializer=lambda v: json.dumps(v).encode('ascii'))
            producer.send(
            TOPIC_POST_VIDEO,
            key={"video-event": 'POST'},
            value={
                "user_id": user_id,
                "title": request.form.get("title"),
                "resume": request.form.get("resume"),
                "category_id": category_id, 
                "category" : request.form.get("category")
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
def get_video(video_id):
    video = client.get_video(video_id=video_id)
    return render_template('video.html', video=video.videos)


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


@content.route('/profile')
@login_required
def profile():
    user_content = client.get_latest_videos_user(current_user.user_id)
    if user_content:
        user_content = user_content.videos
    return render_template('profile.html', name=current_user.name, user_content=user_content)
    



@content.route('/watch-video/<int:id>', methods=['POST'])
def video_watched_event(id):
    try:
        #user_id = current_user.user_id

        producer = KafkaProducer(
        bootstrap_servers='kafka1:9092', 
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii'))
        producer.send(
        TOPIC_WATCHED_VIDEO,
        key={"video_id": id},
        value={
            "user_id": 1
        })
        producer.flush()
        return 'Video successfully watched'
    except Exception as e:
        print(str(e))
        return 'Video watch event failed'
    

@content.route('/rate-video', methods=['POST'])
def video_rated_event():
    try:
        rating = request.form.get('rating')
        video_id = request.form.get('current_video')
        #user_id = current_user.user_id


        producer = KafkaProducer(
        bootstrap_servers='kafka1:9092', 
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii'))
        producer.send(
        TOPIC_RATE_VIDEO,
        key={"video_id": video_id},
        value={
            "user_id": 1,
            "rating" : rating
        })
        producer.flush()
        return 'Video successfully rated'
    except Exception as e:
        print(str(e))
        return 'Video rate event failed'
  