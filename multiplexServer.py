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


# Functions

def addPlayer(playerName): #adds player to players-list and checks/Assigns for master-client if affordable
    for player in players:
        if player == playerName:
            return True

    players.append(playerName)
    masterClientDefined = False
    for player in players:
        if player[-6:] == "master":
            masterClientDefined = True

    if masterClientDefined is False:
        players[0] = players[0] + "_master"

    print players


while True:  # main loop

    time.sleep(0.1)
    try:
        lesen, schreiben, oob = select.select([server] + clients, [], [], 0.0)
    except Exception, e:
        print str(e)

    for sock in lesen:
        if sock is server:
            client, addr = server.accept()
            clients.append(client)
            print "Client verbunden"
            # registerPlayer(str(addr))
            client.send("hi")

        else:
            try:  # receive data from client
                nachricht = sock.recv(1024).decode('utf-8')
                nachricht = str(nachricht)

                addPlayer(nachricht.split('_')[0])
            except:
                print "Player Connection lost"
                clients.remove(sock)
                # definePlayerName(str(sock.getpeername()), nachricht.split('_')[0])

                # if nachricht:
                #   stuffToSend += nachricht
                # else:
                #   print "Socket beendet"
                #  sock.close()
                # clients.remove(sock)

    for client in clients:  # sends availabel data in stufftosend to all clients
        try:
            client.send(stuffToSend)
        except:
            print "player connection lost"
            clients.remove(client)

    stuffToSend = "."
