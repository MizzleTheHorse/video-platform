import grpc
import time
import user_service_pb2
import user_service_pb2_grpc


def run():
    print("Running forever...")
    while True:
        with grpc.insecure_channel('localhost:50051') as channel:

            print('starting test')
            print(' ')
            stub = user_service_pb2_grpc.UserServiceStub(channel)

            print("Calling function -> GetUser")
            response = stub.GetUser(user_service_pb2.UserRequest(name='test', email='test1'))
            if not response.response_code == 200:
                print('User not found')
            else:
                print("Fetched user. ID: " + str(response.user_id))

            time.sleep(2)
            print(' ')
            print('Calling function -> PostUser')
            response = stub.PostUser(user_service_pb2.UserRequest(name='test', email='test1', hashed_password='sha256$eGVkT8qf4rSuXFCt$7769b1d9349a2a25001b25baca787ef00be96377ebf446a97127435fcebb1b9a'))
            if not response.response_code == 200:
                print('user already exists')
            else:
                print("Inserted user. ID: " + str(response.user_id))

            time.sleep(2)
            print(' ')


            response = stub.GetUser(user_service_pb2.UserRequest(name='test', email='test1'))
            if not response.response_code == 200:
                print('user not found')
                
            else:
                print("Fetched user. ID: " + str(response.user_id))

            time.sleep(2)
            print(' ')

            response = stub.DeleteUser(user_service_pb2.UserRequest(name='test', email='test_mail11', hashed_password='&%¤#"!'))
            if not response.response_code == 200:
                print('user not found')
            else:
                print("Deleted user. " + str(response.user_id))
                return
        
            time.sleep(1)
            print(' ')

       
if __name__ == '__main__':
    run()
