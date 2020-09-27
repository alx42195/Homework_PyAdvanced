"""
Задание 1
Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте
загрузить данные из файла
"""
import os.path
import json


data = [{"test x": x-40, "test y": x-10, "test z": x+20} for x in range(50, 60)]

with open(os.path.join("data", "test.json"), "w") as wfile:
    json.dump(data, wfile, indent=4)

with open(os.path.join("data", "test.json")) as rfile:
    result = json.load(rfile)
    print(result)