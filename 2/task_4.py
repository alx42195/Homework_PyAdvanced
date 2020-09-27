"""
Задание 4
Для таблицы «материала» из дополнительного задания создайте пользовательскую агрегатную
функцию, которая считает среднее значение весов всех материалов результирующей выборки и
округляет данной значение до целого.
"""

import sqlite3
import json

def multiplication(num):
    return num * 10

def adapt_json(data):
    return json.dumps(data)

def convert_json(raw):
    return json.loads(raw)

sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

cur.execute('CREATE TABLE "materials" (id, weight, height, additional_properties)')

cur.execute(
    """INSERT INTO materials(id, weight, height, additional_properties)
        VALUES (1, 100, 200, ?), ({'temperature': 20, 'density': 1.5})
    """
)
cur.execute(
    'SELECT additional_properties FROM materials'
)
result = cur.fetchall()
print(result)


"""
Над этим заданием застопорился, чувствую нужно сначала выучить SQL, перед выполнением таких заданий
sqlite3.OperationalError: unrecognized token: "{"

В чем проблема?
Хочу сначала научить SQL при помощи адаптера распознавать словарь или кортеж, а затем создать агрегатную функцию

"""