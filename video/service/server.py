from concurrent import futures
import grpc
from kafka import KafkaConsumer, KafkaProducer
import video_service_pb2
import video_service_pb2_grpc
from ORM_CRUD_videos import DatabaseInterface

class VideoService():
    

    def __init__(self) -> None:
        self.db = DatabaseInterface()


    def GetVideo(self, request, context):
        if request.latest:
            if request.category:
                #return latest videos in a certain category
                video_list = self.db.get_latest_videos(category=request.category)
                return video_service_pb2.VideoResponse(videos = video_list, response_code = 'ok')
            #return latest videos
            video_list = self.db.get_latest_videos()
            return video_service_pb2.VideoResponse(videos = video_list, response_code = 'ok')
        
        if request.video_id and request.user_id:
            video = self.db.get_video(id=request.video_id)
            video_list = []
            video_list.append(video)
            #return video with ID
            return video_service_pb2.VideoResponse(videos = video_list, response_code = 'ok')
        return video_service_pb2.VideoResponse(response_code = 'no videos found')
        

    def PostVideo(self, request, context):
        video = request.video
        print(type(video))
        video = self.db.post_video(user_id=request.user_id, title=request.title, resume=request.resume, category=request.category)
        if video:
            return video_service_pb2.VideoResponse(response_code = 'ok')
        return video_service_pb2.VideoResponse(response_code = 'no videos found')


    def DeleteVideo(self, request, context):
        video = self.db.delete_video(video_id=request.video_id)
        if video == 'not found':
            return video_service_pb2.VideoResponse(response_code = 'no videos found')
        return video_service_pb2.VideoResponse(response_code = 'ok')

    

def serve_consumer():
    raise NotImplementedError


def serve_gRPC():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    video_service_pb2_grpc.add_UserServiceServicer_to_server(VideoService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve_gRPC()