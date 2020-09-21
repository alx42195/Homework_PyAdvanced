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
CLIENT = socket(AF_INET, SOCK_DGRAM)

msg = "Device 456"
CLIENT.sendto(msg.encode("utf-8"), SOCKADDR)

CLIENT.close()