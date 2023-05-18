from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask, request, render_template, Response, stream_with_context
from flask import current_app as app
from flask_login import current_user, login_required 
import requests
#from .models import Video
from kafka import KafkaConsumer, KafkaProducer
import json
import os
from .video_client import VideoClient

recommendation = Blueprint('recommendation', __name__)
client = VideoClient()
recommendation_ip = os.getenv("RECOMMENDATION_IP")
url = f'http://{recommendation_ip}:80/'

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

@recommendation.route('/recommended')
def recommend():
    #r = requests.get(url +'random_recommend')

    video = client.get_latest_videos()
    video_list = []
    if not video:
        flash('No videos are available yet, be the first to upload!')
        return redirect(url_for('content.video'))
    for x in video.videos:
        video_list.append(x)
    video_list.reverse()
    return render_template('recommended.html', content=video_list)



@recommendation.route('/recommended/<int:user_id>')
@login_required
def recommend_user(user_id):
    request = requests.get(url +'recommend/'+str(user_id))
    data = request.json()
    if data == 'Not Found':
        flash('No videos watched or liked yet, viewing random recommendations')
        return redirect(url_for('recommendation.recommend'))

    category_id = category_to_watch(data)
    content = client.get_latest_videos_category(category_id)
    if not content:
        flash('No videos are available for this category')
        return redirect(url_for('content.category'))
    return render_template('recommended.html', content=content.videos)


def category_to_watch(data):
    list = []
    for x in data.values():
        list.append(x)
    video = most_frequent(list)
    content = client.get_video(video_id=int(video))
    return content.videos[0].category_id
    

def most_frequent(List):
    return max(set(List), key = List.count)