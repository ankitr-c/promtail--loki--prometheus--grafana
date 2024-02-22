from flask import Flask
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Gauge

app = Flask(__name__)

request_count = Counter('request_count', 'Total Request Count')
current_users = Gauge('current_users', 'Number of current users') 

@app.route('/')
def hello():
    current_users.inc()
    request_count.inc()
    return 'Hello World!'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)