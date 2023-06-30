import socket
from _thread import *
import sys

server = "192.168.1.2"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server, port))
    s.listen(2)
    print("Waiting for connection. Server started.")

    def read_pos(str):
        str = str.split(",")
        return int(str[0]), int(str[1])

    def make_pos(tup):
        return str(tup[0])+","+str(tup[1])

    pos = [(0, 0), (100, 100)]

    def threaded_client(conn, current_player):
        conn.send(str.encode(make_pos(pos[current_player])))
        reply = ""
        while True:
            try:
                data = read_pos(conn.recv(2048).decode())
                pos[current_player]=data

                if not data:
                    print("Disconnected")
                    break
                else:
                    if current_player==1:
                        reply=pos[0]
                    else:
                        reply=pos[1]
                    print("Received:", data)
                    print("Sending:", reply)
                conn.sendall(str.encode(make_pos(reply)))
            except:
                break
        print("Lost Connection")
        conn.close()
    current_player = 0
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, current_player))
        current_player += 1
