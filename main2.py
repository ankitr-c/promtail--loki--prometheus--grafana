from flask import Flask
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Gauge, Counter, Histogram
import psutil
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Custom metrics
request_count = Counter('request_count', 'Total Request Count')
current_users = Gauge('current_users', 'Number of current users')

# System metrics
cpu_usage = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage = Gauge('memory_usage', 'Memory usage percentage')
disk_usage = Gauge('disk_usage', 'Disk usage percentage')

# Histogram to track request duration
request_duration = Histogram('request_duration_seconds', 'Request duration in seconds')

@app.route('/')
def hello():
    current_users.inc()
    request_count.inc()
    return 'Hello World!'

@app.route('/metrics')
def metrics():
    # Update system metrics
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)

    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/slow')
def slow_endpoint():
    import time
    start_time = time.time()
    time.sleep(2)  # Simulate a slow endpoint
    duration = time.time() - start_time
    request_duration.observe(duration)
    return 'Slow endpoint!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
