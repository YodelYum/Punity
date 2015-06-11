__author__ = 'Alex'

import socket
import time
import datetime


waitingTime = 0
start_time = time.time()
stuffToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 50000))

thestring = "thestring"

try:
    while True:
        #time.sleep(0.11)
        time.sleep(0.1)
        s.send(thestring.encode())



finally:
        s.close()
        print "finished"