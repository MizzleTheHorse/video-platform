from concurrent import futures
import grpc
import video_service_pb2
from video_service_pb2 import Video, Category

import video_service_pb2_grpc
from ORM_CRUD_videos import DatabaseInterface

class VideoService():
    
    def __init__(self) -> None:
        self.db = DatabaseInterface()


    def GetVideo(self, request, context):
        try:
            #return latest videos
            if request.latest == True:  
                #return with a specific category
                if request.category_id:
                    video_list = self.db.get_latest_videos_category(category_id=request.category_id)
                    if not video_list:
                        return video_service_pb2.VideoResponse(response_code = 'no videos found')
                    videos = []
                    for x in video_list:
                        video = Video(user_id = x.user_id, video_id = x.video_id, title = x.title, resume = x.resume, category=x.category, category_id = x.category_id)
                        videos.append(video)
                    return video_service_pb2.VideoResponse(videos = videos, response_code = 'ok')
                            
                video_list = self.db.get_latest_videos()
                #if no videos, return none
                if video_list == None:
                    return video_service_pb2.VideoResponse(response_code = 'no videos found')
                videos = []
                for x in video_list:
                    video = Video(user_id = x.user_id, video_id = x.video_id, title = x.title, resume = x.resume, category=x.category, category_id = x.category_id)
                    videos.append(video)
                return video_service_pb2.VideoResponse(videos = videos, response_code = 'ok')
            #get 1 video 
            if request.video_id:
                model = self.db.get_video(video_id=request.video_id)
                video = Video(user_id = model.user_id, video_id = model.video_id, title = model.title, resume = model.resume,  category_id = model.category_id, category=model.category)
                video_list = []
                video_list.append(video)
                #return video with ID
                return video_service_pb2.VideoResponse(videos = video_list, response_code = 'ok')
            #get all videos from specific user
            if request.user_id:
                video_list = self.db.get_latest_videos_user(id=request.user_id)
                #if no videos, return none
                if not video_list:
                    return video_service_pb2.VideoResponse(response_code = 'no videos found')
                videos = []
                for x in video_list:
                    video = Video(user_id = x.user_id, video_id = x.video_id, title = x.title, resume = x.resume,  category_id = x.category_id, category=x.category)
                    videos.append(video)
                #return video with ID
                return video_service_pb2.VideoResponse(videos = videos, response_code = 'ok')
            return video_service_pb2.VideoResponse(response_code = 'no videos found')
        except Exception as e:
            return video_service_pb2.VideoResponse(response_code = str(e))

        
    #Get all categories
    def GetCategories(self, request, context):
        categories = self.db.get_categories()
        if not categories:
            return video_service_pb2.CategoryResponse(response_code = 'no videos found')
        category_list = []
        for x in categories:
            category = Category(category_id = x.category_id, category = x.category)
            category_list.append(category)
        return video_service_pb2.CategoryResponse(categories = category_list, response_code = 'ok')
    
    


def serve_gRPC():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    video_service_pb2_grpc.add_VideoServiceServicer_to_server(VideoService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Content Management Service Started on: " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve_gRPC()