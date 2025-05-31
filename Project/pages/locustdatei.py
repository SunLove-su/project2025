from locust import HttpUser,task,between 
import os

class AppUser(HttpUser):
    wait_time = between(2,5)

    
    def login(self):
        basis_passwort = os.getenv("UMFRAGE_PASSWORT")
            self.client.post("/", { "Passwort": "basis_passwort"})

    @task
    def startseite(self):
        self.client.get("/")

    @task
    def einstiegsumfrage(self):
        self.client.get("/Umfrage")
        data = {
            "alter": "Unter 15 Jahre",
            "geschlecht" :"weiblich",
            "ki_wissen" : "sehr gut"
            }
        self.client.post("/Umfrage", data=data)

    #Übung_1
    @task
    def uebung1(self):
        self.client.get("/Übung_1")
        frage = "Wer ist der atuelle Präsident der USA"
        
        self.client.post("/Übung_1", data = {"frage": frage, "senden": "Fragen"})
