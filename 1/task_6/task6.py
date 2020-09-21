"""
Задание 6
Используя сервис https://jsonplaceholder.typicode.com/ попробуйте построить различные типы
запросов и обработать ответы. Необходимо попрактиковаться с urllib и библиотекой requests.
Рекомендуется сначала попробовать выполнить запросы, используя urllib, а затем попробовать
реализовать то же самое используя requests.
"""
from urllib import request as rq
import requests

URL = "https://jsonplaceholder.typicode.com/"
msg = rq.urlopen(URL)
load = {
    "login" : "user123",
    "password": "123456",
}

print(msg.status)
print(msg.getcode())
print(msg.msg)
print(msg.reason)
print(msg.headers)
print(msg.getheaders())
print(msg.headers.get('Content-Type'))
print(msg.getheader('Content-Type'))

print(requests.get(URL).status_code)
print(requests.get(URL).headers)
print(requests.post(URL).status_code)
