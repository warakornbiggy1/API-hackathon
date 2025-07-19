from flask import Flask
import os

app = Flask(__name__)
PORT = os.getenv('PORT', 5001)

@app.route('/')
def hello_world():
    print("API2: Received a request and sending 'Hello from API2!'")
    return "Hello from API2!"

if __name__ == '__main__.':
    app.run(host='0.0.0.0', port=PORT)