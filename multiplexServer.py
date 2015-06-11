__author__ = 'Alex'

import socket
import select
import time
import datetime
import sys

waitingTime = 0
start_time = time.time()
stuffToSend = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 50000))
server.listen(1)

clients = []

try:
    while True:

        time.sleep(0.05)

        lesen, schreiben, oob = select.select([server] + clients, [], [],0)

        for sock in lesen:
            if sock is server:
                client, addr = server.accept()
                clients.append(client)
                print "Client verbunden"
            else:
                nachricht = sock.recv(1024).decode('utf-8')
                nachricht = str(nachricht)
                if nachricht:


                    stuffToSend += nachricht
                else:
                    print "Socket beendet"
                    sock.close()
                    clients.remove(sock)
        print stuffToSend
        stuffToSend = ""
                    # send data

finally:
    for c in clients:
        c.close()
    server.close()
