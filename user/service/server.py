import grpc, sys
from datetime import datetime
import user_service_pb2
import user_service_pb2_grpc
from ORM_CRUD_users import DatabaseInterface


from concurrent import futures


#UserService class
#Functions returns UserReply. With either 200 if operation success or 404 if failure
class UserService(user_service_pb2_grpc.UserServiceServicer):

    def __init__(self):
        self.db = DatabaseInterface()

    
    def GetUser(self, request, context):
        if not request.user_id:
            print('Recieved GET request: ' + request.email + ". " + str(datetime.now()) + " \n")
            user = self.db.get_user(email=request.email)
            if user:
                print('Sent GET reply success: ' + request.email + ". " +  str(datetime.now()) + " \n")
                return user_service_pb2.UserReply(user_id=user.user_id, name=user.name, email=user.email, hashed_password=user.hashed_password, response_code=200)
            else: 
                print('Sent GET reply failure. ' + str(datetime.now()) + " \n")
                return user_service_pb2.UserReply(response_code=404)
        else:
            print('Recieved GET_ID request: ' + str(request.user_id) + ". "+ str(datetime.now()) + " \n")
            user = self.db.get_user_by_id(user_id=request.user_id)
            if user:
                print('Sent GET_ID reply success: ' + str(request.user_id) + ". " + str(datetime.now()) + " \n")
                return user_service_pb2.UserReply(user_id=user.user_id, name=user.name, email=user.email, hashed_password=user.hashed_password, response_code=200)
            else: 
                print('Sent GET_ID reply failure: ' + str(request.user_id) + ". "+ str(datetime.now())+ " \n") 
                return user_service_pb2.UserReply(response_code=404)
                

    def PostUser(self, request, context):
        print('Recieved  POST request: ' + request.email + ". " + str(datetime.now()) + " \n")
        user = self.db.post_user(name=request.name, email=request.email, hashed_password=request.hashed_password)
        if user:
            print('Sent POST reply success: ' + request.email + ". " + str(datetime.now()) + " \n")
            return user_service_pb2.UserReply(user_id=user.user_id, name=user.name, email=user.email, hashed_password=user.hashed_password, response_code=200)
        print('Sent POST reply failure: ' + request.email + ". " + str(datetime.now()) + " \n")
        return user_service_pb2.UserReply(response_code=404)


    def DeleteUser(self, request, context):
        user = self.db.delete_user(email=request.email)
        if user == 'not found':
            return user_service_pb2.UserReply(response_code=404)
        return user_service_pb2.UserReply(user_id=user.user_id, response_code=200)


    def GetUserDepr(self, request, context):
        if request.user_id: 
            user = self.db.get_user(id=request.user_id, email=request.email)
            if user == 'not found':
                return user_service_pb2.UserReply(response_code=404)
            return user_service_pb2.UserReply(user_id=user.user_id, name=user.name, email=user.email, hashed_password=user.hashed_password, response_code=200)
        else: 
            user = self.db.get_user(email=request.email)
            if user == 'not found':
                return user_service_pb2.UserReply(response_code=404)
            print(user)
            return user_service_pb2.UserReply(user_id=user.user_id, name=user.name, email=user.email, hashed_password=user.hashed_password, response_code=200)
    


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("User Service Started on:" + port)
    server.wait_for_termination()


def consume_events():
    raise NotImplementedError


if __name__ == '__main__':
    serve()