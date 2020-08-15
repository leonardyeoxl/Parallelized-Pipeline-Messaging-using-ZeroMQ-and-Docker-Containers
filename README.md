# Parallelized Pipeline Messaging using ZeroMQ and Docker Containers

![Parallelized Pipeline Messaging](./zmq-docker-streamer.jpg)

## Build

```sh
~/zmq-docker-streamer$ docker-compose build
```

## Scale

```sh
~/zmq-docker-streamer$ docker-compose scale worker=2
Creating and starting zmqdockerstreamer_worker_1 ... done
Creating and starting zmqdockerstreamer_worker_2 ... done
```

## Run

```sh
~/zmq-docker-streamer$ docker-compose up
zmqdockerstreamer_worker_2 is up-to-date
zmqdockerstreamer_worker_1 is up-to-date
Creating zmqdockerstreamer_device_1
Creating zmqdockerstreamer_producer_1
Attaching to zmqdockerstreamer_worker_2, zmqdockerstreamer_worker_1, zmqdockerstreamer_device_1, zmqdockerstreamer_producer_1
worker_1    | I am consumer #8150
worker_2    | I am consumer #6297
worker_1    | {'consumer': 8150, 'num': 0}
worker_1    | {'consumer': 8150, 'num': 1}
worker_1    | {'consumer': 8150, 'num': 2}
worker_2    | {'consumer': 6297, 'num': 3}
worker_1    | {'consumer': 8150, 'num': 4}
worker_2    | {'consumer': 6297, 'num': 5}
worker_1    | {'consumer': 8150, 'num': 6}
worker_2    | {'consumer': 6297, 'num': 7}
worker_1    | {'consumer': 8150, 'num': 8}
worker_2    | {'consumer': 6297, 'num': 9}
worker_1    | {'consumer': 8150, 'num': 10}
worker_2    | {'consumer': 6297, 'num': 11}
worker_1    | {'consumer': 8150, 'num': 12}
```