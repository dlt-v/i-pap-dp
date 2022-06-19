
import socket
from _thread import start_new_thread
import sys

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

pos = [(0, 0), (100, 100)]


def read_pos(str: str):
    '''
    Convert a string into a tuple with player coordinates.
    '''
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup) -> str:
    '''
    Convert a tuple with player coordinates into a string.
    '''
    return f"{tup[0]},{tup[1]}"


def threaded_client(conn, player: int):
    conn.send(str.encode(make_pos(pos[player])))

    reply = ""
    while True:
        try:

            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected.")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending:", reply)

            conn.sendall(str.encode(make_pos(reply)))
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
