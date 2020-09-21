"""
Задание 1
Создать простой чат, на основе TCP протокола, который позволит подключаться нескольким
клиентам и обмениваться сообщениями.
"""

import socket
from threading import Thread


sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST = "127.0.0.1"
HOST = "192.168.0.66"
PORT = 9999
BUFFSIZE = 1024
SOCK_CLIENT_ADDR = (HOST, PORT)

sock_client.connect(SOCK_CLIENT_ADDR)

def receive():
    while True:
        data = sock_client.recv(BUFFSIZE)
        print(f"\n{data.decode('utf-8')}")

def send():
    while True:
        # message = pretext + input(f"Your new message output > ")
        message = pretext + input()
        if message == pretext + "quit":
            sock_client.close()
            break
        else:
            sock_client.send(message.encode("utf-8"))

if __name__ == "__main__":
    me = input("Please enter your name > ")
    pretext = me + " says: "
    receiving_THREAD = Thread(target=receive)
    sending_THREAD = Thread(target=send)
    receiving_THREAD.start()
    sending_THREAD.start()


