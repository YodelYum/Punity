__author__ = 'Alex'

import socket
import select
import time
import datetime
import sys

waitingTime = 0
start_time = time.time()
stuffToSend = ""
ticker = 20

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 50000))
server.listen(1)

clients = []
players = []


#Functions

def registerPlayer(ip): #called when new client connects, adds players IP to players-array
    players.append(ip)
    #if len(players) is 1:
        #players[0] = players[0] + "_master"

    players

def definePlayerName(ip, playerName): #checks if there are still IPs in clients[] and checks for names
    try:
        theIndex = clients.index(str(ip))
        clients[theIndex] = str(playerName)
    except:
        clients.append(str(playerName))

try:
    while True: #main loop

        time.sleep((1/ticker))
        lesen, schreiben, oob = select.select([server] + clients, [], [],0)

        for sock in lesen:
            if sock is server:
                client, addr = server.accept()
                clients.append(client)
                registerPlayer(str(addr))
                print "Client verbunden"
            else:
                nachricht = sock.recv(1024).decode('utf-8')
                nachricht = str(nachricht)
                definePlayerName(sock.getpeername(),nachricht.split('_')[0])
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
