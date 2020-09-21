"""
Задание 1
Создать простой чат, на основе TCP протокола, который позволит подключаться нескольким
клиентам и обмениваться сообщениями.
"""

import socket
from threading import Thread

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST = "127.0.0.1"
HOST = "192.168.0.66"
PORT = 9999
BUFFSIZE = 1024
SOCK_SERV_ADDR = (HOST, PORT)
sock_server.bind(SOCK_SERV_ADDR)
clients = {}
sockets_book = {}

def accepting_connections():
    while True:
        client, client_address = sock_server.accept()
        sockets_book[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    while True:
        data = client.recv(BUFFSIZE)
        broadcast(data)

def broadcast(msg):
    for sock in sockets_book:
        sock.send(msg)


if __name__ == "__main__":
    sock_server.listen(5)
    ACCEPT_THREAD = Thread(target=accepting_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    sock_server.close()





