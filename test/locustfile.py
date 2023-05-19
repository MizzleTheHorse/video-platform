from locust import HttpUser, TaskSet, task, between
import time
import random



def get_random():
    return random.randint(0,10000)


class UserBehavior(HttpUser):
    
    wait_time = between(0.5, 10)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.sign_up_and_login()
        

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()
    
    
    def sign_up_and_login(self):
        random = get_random()
        self.client.post('/signup', {"email":"test" + str(random) + "@test.dk", "name":"test", "password": "test"})
        time.sleep(0.5)
        self.login(random_int=random)


    def login(self, random_int):
        self.client.post("/login", {"username":"test" + str(random_int) + "@test.dk", "password":"test"})
    

    def logout(self):
        self.client.get('/logout')

    
    @task(1)
    def profile(self):
        self.client.get('/profile')
    '''
    @task(1)
    def index(self):
        self.client.get('/')

    @task(1)
    def latest(self):
        self.client.get('/latest')

    @task(1)
    def recommended(self):
        self.client.get('/recommended')

    @task(1)
    def get_video(self):
        for item_id in range(1, 7):
            self.client.get(f"/video/{item_id}")
            time.sleep(1)

    @task(1)
    def watch_video(self):
        for item_id in range(1, 7):
            self.client.post(f"/watch-video/{item_id}")
            time.sleep(1)

    @task(1)
    def rate_video(self):
        for item_id in range(1, 7):
            self.client.post(f"/rate-video" , {"video_id": item_id, "category_id": 1})
            time.sleep(1)

    @task(1)
    def upload_video(self):
        self.client.post("/video", {"title":"test-title", "category":"Programming", "resume": "This is a test resume"})
    '''
