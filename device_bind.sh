#!/bin/bash
echo "running streamer device 1"
python streamer_device1.py &
echo "running streamer device 2"
python streamer_device2.py &
while true; do sleep 1; done