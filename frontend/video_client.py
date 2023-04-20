import os, grpc, sys
sys.path.append('.')
from video_service_pb2 import VideoRequest
from video_service_pb2_grpc import VideoServiceStub
from .models import User

video_service_host = os.getenv("VIDEO_SERVICE_HOST", "localhost")
video_service_channel = grpc.insecure_channel(
    f"{video_service_host}:50051"
)

video_client = VideoServiceStub(video_service_channel)


class VideoClient():
    def __init__(self) -> None:
        pass
    
    def get_latest_videos(self):
        request = VideoRequest(latest=True)
        response = video_client.GetVideo(request)
        if not response.response_code =='ok':
            return None
        return response
    
    def get_latest_videos_category(self, category_id):
        request = VideoRequest(latest=True, category_id=category_id)
        response = video_client.GetVideo(request)
        if not response.response_code =='ok':
            return None
        return response
    
    def get_video(self, video_id):
        request = VideoRequest(video_id=video_id)
        response = video_client.GetVideo(request)
        if not response.response_code =='ok':
            return None
        return response
    
    
    def get_latest_videos_user(self, user_id):
        request = VideoRequest(user_id=user_id)
        response = video_client.GetVideo(request)
        if not response.response_code =='ok':
            return None
        return response
    