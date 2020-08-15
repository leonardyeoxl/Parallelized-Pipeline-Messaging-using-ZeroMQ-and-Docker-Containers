import sys
import time
import zmq
import random
import os

def end_of_pipeline():
    ZMQ_END_OF_PIPELINE_ADDRESS = os.environ["ZMQ_END_OF_PIPELINE_ADDRESS"]
    end_of_pipeline_id = random.randrange(1,10005)
    print("I am end #{}".format(end_of_pipeline_id))
    
    context = zmq.Context()
    # recieve work
    end_of_pipeline_receiver = context.socket(zmq.PULL)
    end_of_pipeline_receiver.connect(ZMQ_END_OF_PIPELINE_ADDRESS)

    while True:
        work = end_of_pipeline_receiver.recv_json()
        data = work['num']
        worker_id = work['worker']
        result = { 'end_of_pipeline_id' : end_of_pipeline_id, 'worker_id': worker_id, 'num' : data}
        print(result)

end_of_pipeline()