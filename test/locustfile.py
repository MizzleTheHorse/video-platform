from test.locustfile import HttpUser, task, between
import time

class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2.5)

    @task
    def index(self):
        self.client.get('/')

    @task
    def latest(self):
        self.client.get('/latest')

    @task
    def get_video(self):
        for item_id in range(1, 7):
            self.client.get(f"/video/{item_id}")
            time.sleep(0.5)
    
    @task
    def watch_video(self):
        for item_id in range(1, 7):
            self.client.get(f"/video/{item_id}")
            time.sleep(0.5)
    
    
    