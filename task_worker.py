import sys
import time
import zmq
import random
import os

def worker():
    ZMQ_WORKER_ADDRESS = os.environ["ZMQ_WORKER_ADDRESS"]
    ZMQ_WORKER_TO_END_OF_PIPELINE_ADDRESS = os.environ["ZMQ_WORKER_TO_END_OF_PIPELINE_ADDRESS"]
    worker_id = random.randrange(1,10005)
    print("I am worker #{}".format(worker_id))

    context = zmq.Context()
    # recieve work
    worker_receiver = context.socket(zmq.PULL)
    worker_receiver.connect(ZMQ_WORKER_ADDRESS)

    # send work
    worker_sender = context.socket(zmq.PUSH)
    worker_sender.connect(ZMQ_WORKER_TO_END_OF_PIPELINE_ADDRESS)

    while True:
        work = worker_receiver.recv_json()
        data = work['num']
        result = { 'worker' : worker_id, 'num' : data }
        print(result)
        worker_sender.send_json(result)

worker()