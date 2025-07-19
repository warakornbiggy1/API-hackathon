from flask import Flask, request
import requests
import os

app = Flask(__name__)
PORT = os.getenv('PORT', 5000)
API2_URL = os.getenv('API2_URL', 'http://api2:5001') # กำหนดชื่อ Service ของ API2 ตาม docker-compose

@app.route('/')
def proxy_to_api2():
    print("API1: Received a request from user.")
    try:
        response = requests.get(API2_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        api2_response = response.text
        print(f"API1: Successfully forwarded request to API2 and got response: '{api2_response}'")
        return f"API1: Forwarded request to API2. API2 says: {api2_response}"
    except requests.exceptions.RequestException as e:
        print(f"API1: Error forwarding request to API2: {e}")
        return f"API1: Error connecting to API2: {e}", 500

if __name__ == '__main__.':
    app.run(host='0.0.0.0', port=PORT)