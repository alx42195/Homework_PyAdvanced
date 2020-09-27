"""
Задание 2
Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота и доп.
характеристики материала. Поле доп. характеристики материала должно хранить в себе массив,
каждый элемент которого является кортежем из двух значений, первое – название
характеристики, а второе – её значение
"""

import sqlite3

conn = sqlite3.connect(':memory:')

conn.execute('CREATE TABLE "materials" (id, weight, height, additional_properties)')

conn.execute(
    """INSERT INTO materials(id, weight, height, additional_properties)
        VALUES (1, 100, 200, "('temperature', 20), ('density', 1.5)"),
                (2, 200, 100, "('temperature', 30), ('density', 2.5)"),
                (3, 300, 400, "('temperature', 10), ('density', 0.5)")   
    """
)

data = conn.execute('SELECT * FROM "materials"').fetchall()
print(data)