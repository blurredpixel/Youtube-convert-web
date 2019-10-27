from locust import HttpLocust, TaskSet
from random import randint
titles=[]
# class extras():
#     artist="TheEagles"
#     randnum=randint(1,10000)
#     title="Test{}".format(randnum)
#     path="/downloads/{}-{}.mp3".format(title,artist)

class UserBehavior(TaskSet):
    def __init__(self, *args, **kwargs):
        super(UserBehavior, self).__init__(*args, **kwargs)
    # Each locust user gets a different id
        self.random_id = str(randint(1,10000))
    
    
    def index(self):
        self.client.get("/")
    def convert(self):
        
        artist="TheEagles"
        
        title="Test{}".format(self.random_id)
        path="/downloads/{}-{}.mp3".format(title,artist)
        titles.append(path)
        print("Titles size: {}".format(len(titles)))
        self.client.post("/",{"videourl":"https://www.youtube.com/watch?v=7PCkvCPvDXk","title":title,"artist":artist})
        
    def download(self):
        path=titles.pop()
        print("downloading path: {}".format(path))
        self.client.get("{}".format(path))
    def on_start(self):
        
        self.index()
        
    tasks = {index: 1,convert: 6, download:6}
    # def on_stop(self):
    #     self.download(titles.pop())
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000