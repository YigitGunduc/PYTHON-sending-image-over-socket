"""
Created on July 3 2020
@author: Yigit GUNDUC
"""

import socket
import time
import pickle
import cv2

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1244))
s.listen(5)

while True:

    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = cv2.imread("image PATH",3)
    
    print(d)
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    print(msg)
    clientsocket.send(msg)