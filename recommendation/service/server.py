from concurrent import futures
import grpc
import video_service_pb2
from video_service_pb2 import Video, Category

import video_service_pb2_grpc
from ORM_CRUD_videos import DatabaseInterface


class VideoService():
    
    def __init__(self) -> None:
        self.db = DatabaseInterface()
        

    def GetUserRecommendation(self):
        #get users most liked video 
        #db.get_video_id(user_id)
        #find the most watched category 
        #return videos of the most watched category 
        pass


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