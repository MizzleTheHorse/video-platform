import grpc
import time
import video_service_pb2
import video_service_pb2_grpc


def run():
    print("Running forever...")
    while True:
        with grpc.insecure_channel('localhost:50051') as channel:

            print('starting test')
            print(' ')
            stub = video_service_pb2_grpc.VideoServiceStub(channel)

            print("Get Video")

            video1 = video_service_pb2.Video()

            video1.user_id = 1
            video1.title = 'oskar sutter neger nosser'
            video1.resume = 'ja det kan du tro han gør'
            video1.category = 'faggotroni'

            response = stub.GetVideo(video_service_pb2.VideoRequest(user_id = 1, Video=video1))
            print(response)

            time.sleep(2)

            print('Get Latest')

            response = stub.GetVideo(video_service_pb2.VideoRequest(latest=True))
            print(response)

            time.sleep(2)

       
if __name__ == '__main__':
    run()
