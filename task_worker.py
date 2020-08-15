import sys
import time
import zmq
import random
import os

def consumer():
    ZMQ_WORKER_ADDRESS = os.environ["ZMQ_WORKER_ADDRESS"]
    consumer_id = random.randrange(1,10005)
    print("I am consumer #{}".format(consumer_id))
    
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect(ZMQ_WORKER_ADDRESS)

    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = { 'consumer' : consumer_id, 'num' : data}
        print(result)

consumer()