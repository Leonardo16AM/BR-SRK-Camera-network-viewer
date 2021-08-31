import cv2
import socket
from termcolor import colored
import base64
import zmq
import numpy as np

context=zmq.Context()
client_socket=context.socket(zmq.SUB)
client_socket.bind('tcp://*:5555')
client_socket.setsockopt_string(zmq.SUBSCRIBE,np.unicode(''))

while 1:
    try:
        package = client_socket.recv_string()
        img=base64.b64decode(package)
        npimg=np.fromstring(img,dtype=np.uint8)
        source=cv2.imdecode(npimg,1)
        cv2.imshow('Client',source)
        cv2.waitKey(1)
    except Exception as e:
        print(e)
        break