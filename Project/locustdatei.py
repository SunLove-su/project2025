from locust import HttpUser,task,between 
import os

class AppUser(HttpUser):
    wait_time = between(2,5)

    

    @task
    def startseite(self):
         self.client.get("/")

    