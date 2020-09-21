"""
Задание 1
Изучите основные понятия, рассмотренные в уроке и работу с TCP и UDP протоколами в Python.
Задание 2
Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети. Он принимает
сообщения определенного формата, в котором будет идентификатор устройства и печатает
новые подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный
идентификатор устройства на сервер, уведомляя о своем присутствии.
"""

from socket import socket, AF_INET, SOCK_DGRAM

HOST = "127.0.0.1"
PORT = 9000
SOCKADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_DGRAM)

SERVER.bind(SOCKADDR)
while True:
    try:
        result = SERVER.recv(1024)
        print(result.decode('utf-8') + " connected")
    except KeyboardInterrupt:
        SERVER.close()
        break

SERVER.close()