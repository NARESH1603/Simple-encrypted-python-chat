#!/usr/bin/env python3
import socket
import threading
import time

# variables
PORT = 9999
SERVER = socket.gethostbyname('localhost') # 127.0.0.1
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# creating socket and binding address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Address fami;y for ipv4 and socket streaming
server_socket.bind(ADDR)
