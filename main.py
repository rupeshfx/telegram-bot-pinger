import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Render Pinger is live!"

def ping():
    while True:
        try:
            url = 'https://telegram-bot-xyqv.onrender.com'  # Replace with your actual bot URL
            r = requests.get(url)
            print(f"Pinged {url} | Status: {r.status_code}")
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(600)

import threading
threading.Thread(target=ping).start()

app.run(host='0.0.0.0', port=8080)
