"""
Дополнительное задание

Задание 2
Создайте HTTP клиента, который будет принимать URL ресурса, тип метода и словарь в качестве
передаваемых данных (опциональный). Выполнять запрос с полученным методом на полученный
ресурс, передавая данные соответствующим методом, и печатать на консоль статус код, заголовки
и тело ответа.

"""



import requests

class HttpRequester:
    def __init__(self, urladdr):
        self.urladdr = urladdr

    def action(self, http_method, load=None):
        if http_method == "get":
            return requests.get(self.urladdr)
        elif http_method == "post":
            return requests.post(self.urladdr, data=load)
        elif http_method == "put":
            return requests.put(self.urladdr, data=load)
        elif http_method == "delete":
            return requests.delete(self.urladdr)
        elif http_method == "patch":
            return requests.patch(self.urladdr, data=load)
        elif http_method == "options":
            return requests.options(self.urladdr, data=load)
        elif http_method == "head":
            return requests.head(self.urladdr, data=load)

    def status_code(self):
        return self.status_code

    def headers(self):
        return self.headers

    def content(self):
        return self.content


URL = "http://example.com"
load = {
    "login" : "user123",
    "password": "123456",
}

event1 = HttpRequester(URL)

print(event1.action("get").status_code)
print(event1.action("get").headers)
print(event1.action("get").content.decode('utf-8'))
print(event1.action("post", load).status_code)
print(event1.action("delete", load).status_code)


