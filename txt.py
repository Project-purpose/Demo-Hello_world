# This program adds two numbers
from flask import Flask
from redis import Redis, RedisError
import os
import socket

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
        
num1 = 1.5
num2 = 6.3

# Add two numbers

sum = float(num1) + float(num2)

# Display the sum

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

