import zmq
import os

def main():
    ZMQ_WORKER_SENDER_DEVICE_ADDRESS = os.environ["ZMQ_WORKER_SENDER_DEVICE_ADDRESS"]
    ZMQ_END_OF_PIPELINE_RECIEVER_DEVICE_ADDRESS = os.environ["ZMQ_END_OF_PIPELINE_RECIEVER_DEVICE_ADDRESS"]

    try:
        context = zmq.Context(1)

        worker_sender = context.socket(zmq.PULL)
        worker_sender.bind(ZMQ_WORKER_SENDER_DEVICE_ADDRESS)

        end_of_pipeline_reciever = context.socket(zmq.PUSH)
        end_of_pipeline_reciever.bind(ZMQ_END_OF_PIPELINE_RECIEVER_DEVICE_ADDRESS)
        
        zmq.device(zmq.STREAMER, worker_sender, end_of_pipeline_reciever)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        pass
        worker_sender.close()
        end_of_pipeline_reciever.close()
        context.term()

if __name__ == "__main__":
    main()