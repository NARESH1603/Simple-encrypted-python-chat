#!/usr/bin/env python3
import socket

#varibles
Port = 9999
SERVER = socket.gethostbyname('localhost') # 127.0.0.1
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)
    print(client_socket.recv(2048).decode(FORMAT))
