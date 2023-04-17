import grpc
import time
import video_service_pb2
import video_service_pb2_grpc
from video_service_pb2 import Video

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        print('Client test for getting videos served:')
        stub = video_service_pb2_grpc.VideoServiceStub(channel)
        print(' ')
        #1
        print('1. Get all latest videos (10)')
        response = stub.GetVideo(video_service_pb2.VideoRequest(latest=True))
        print(response)
        time.sleep(2)
        print(' ')
        #2
        print("2. Get all latest videos with category (10)")
        response = stub.GetVideo(video_service_pb2.VideoRequest(latest=True, category_id=7))
        print(response)
        time.sleep(2)
        print(' ')
        #3
        print("3. Get all latest videos from user (10)")
        response = stub.GetVideo(video_service_pb2.VideoRequest(user_id = 10))
        print(response)
        time.sleep(2)
        print(' ')
        #4
        print("4. Get specific video (10)")
        response = stub.GetVideo(video_service_pb2.VideoRequest(video_id = 1))
        print(response)
        time.sleep(2)
        print(' ')
        
if __name__ == '__main__':
    run()
