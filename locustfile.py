from locust import HttpLocust, TaskSet
from random import randint

def index(l):
    l.client.get("/")
def convert(l,title,artist):
    

    l.client.post("/",{"videourl":"https://www.youtube.com/watch?v=7PCkvCPvDXk","title":title,"artist":artist})
def download(l,title,artist):
    l.client.get("/downloads/{}-{}.mp3".format(title,artist))
class UserBehavior(TaskSet):
    
    tasks = {index: 2,convert: 2}
    def on_start(self):
        randnum=randint(1,10000)
        title="Test {}".format(randnum)
        artist="The Eagles"
        index(self)
        convert(self,title,artist)
        download(self,title,artist)
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000