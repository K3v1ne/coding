import requests
from threading import Thread

def guirequest():
        url = "http://127.0.0.1:3333/login.php"
        requests.post(url, data={"jazoest": "2888", "lsd": "AVqK7GczFT0", "email": "LOLOLOLOLOLLOLOLOLOLOLOLOLOLOL", "pass": "LOLOLOLOLOLLOLOLOLOLOLOLOLOLOL", "pass": "LOLOLOLOLOLLOLOLOLOLOLOLOLOLOL", "login_source": "comet_headerless", "next": "", "login": "1"})

counter = 0
while True:
    counter += 1
    t_worker = Thread(target=guirequest)
    t_worker.start()
    print("Đã gửi", counter, "Request đến Server")