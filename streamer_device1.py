import zmq
import os

def main():
    ZMQ_PRODUCER_DEVICE_ADDRESS = os.environ["ZMQ_PRODUCER_DEVICE_ADDRESS"]
    ZMQ_WORKER_DEVICE_ADDRESS = os.environ["ZMQ_WORKER_DEVICE_ADDRESS"]

    try:
        context = zmq.Context(1)
        # Socket facing clients
        producer = context.socket(zmq.PULL)
        producer.bind(ZMQ_PRODUCER_DEVICE_ADDRESS)
        
        # Socket facing services
        worker = context.socket(zmq.PUSH)
        worker.bind(ZMQ_WORKER_DEVICE_ADDRESS)

        zmq.device(zmq.STREAMER, producer, worker)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        pass
        producer.close()
        worker.close()
        context.term()

if __name__ == "__main__":
    main()