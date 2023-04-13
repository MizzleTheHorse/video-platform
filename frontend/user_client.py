import os, grpc, sys
sys.path.append('.')
from user_service_pb2 import UserRequest
from user_service_pb2_grpc import UserServiceStub
from .models import User

user_service_host = os.getenv("USER_SERVICE_HOST", "localhost")
user_service_channel = grpc.insecure_channel(
    f"{user_service_host}:50051"
)

user_client = UserServiceStub(user_service_channel)


class UserClient():
    def __init__(self) -> None:
        pass

    def get_user(self, email):
        request = UserRequest(email=email)
        response = user_client.GetUser(request)
        if response.response_code == 404:
            return None
        user = User(user_id=response.user_id, name=response.name, email=response.email, hashed_password=response.hashed_password)
        return user

    def get_user_by_id(self, user_id):
        request = UserRequest(user_id=user_id)
        response = user_client.GetUser(request)
        if response.response_code == 404:
            return None
        user = User(user_id=response.user_id, name=response.name, email=response.email, hashed_password=response.hashed_password)
        return user

    def post_user(self, user):
        request = UserRequest(name=user.name, email=user.email, hashed_password=user.hashed_password)
        response = user_client.PostUser(request)
        if response.response_code == 404:
            return None
        return response
    
    def delete_user():
        pass
    
