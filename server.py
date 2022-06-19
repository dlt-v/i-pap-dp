
import socket
from _thread import start_new_thread
import sys
import pickle
from Player import Player

server = "172.25.112.1"
port = 5555

# socket(domain, type)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server start: waiting for a connection...")

players = [Player(0, 0, 50, 50, (255, 0, 0)),
           Player(100, 100, 50, 50, (0, 255, 0))]


def threaded_client(conn, player: int):
    conn.send(pickle.dumps(players[player]))

    reply = ""
    while True:
        try:

            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending:", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection.")
    conn.close()


current_player: int = 0

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
