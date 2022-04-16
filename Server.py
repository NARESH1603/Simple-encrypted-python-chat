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
def decrypt(encrypted_message, key):
    outText = []
    cryptText = []
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in encrypted_message:    
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index - key) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index - key) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
        elif eachLetter == ' ':
            outText.append(' ')
    return outText
  
  def handle_client(conn, addr):
    """ Handle clients connection """
    print("[NEW CONNECTION] {0} connected".format(addr))
    connected = True
    while connected:
