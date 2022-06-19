import socket
from _thread import start_new_thread
import sys

server = "192.168.3.7"
port = 5555

# socket(domain, type)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server start: waiting for a connection...")


def threaded_client(conn):
    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected.")
                break
            else:
                print("Received: ", reply)
                print("Sending:", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection.")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, ))
