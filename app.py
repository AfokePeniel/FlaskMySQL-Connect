from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST") or "redis"
redis_port = os.environ.get("REDIS_PORT") or 6379

try:
    r = redis.Redis(host=redis_host, port=redis_port)
    r.ping()
    print("Connected to Redis successfully!")
except redis.exceptions.ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
    exit(1)


@app.route('/')
def index():
    try:
        visits = r.incr('visits')
        return f'Number of visits: {visits}'
    except redis.exceptions.ConnectionError as e:
        return f"Error connecting to Redis: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # host 0.0.0.0 makes it accessible within docker network