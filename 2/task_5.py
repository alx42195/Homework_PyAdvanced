"""
Задание 5
Для таблицы «материала» из дополнительного задания создайте пользовательскую функцию,
которая принимает неограниченное количество полей и возвращает их конкатенацию.

"""

import sqlite3


class RowSet:
    """
    Aggregation function
    """
    def __init__(self):
        self.rows = set()

    def step(self, value):
        self.rows.add(value)

    def finalize(self):
        return ';'.join(self.rows)

conn = sqlite3.connect(':memory:')
conn.create_aggregate('row_set', 1, RowSet)

cur = conn.cursor()
cur.execute('CREATE TABLE "materials" (id, weight, height, additional_properties)')
cur.execute(
    """INSERT INTO materials(id, weight, height, additional_properties)
        VALUES (1, 100, 200, "('temperature', 20), ('density', 1.5)"),
                (2, 200, 100, "('temperature', 30), ('density', 2.5)"),
                (3, 300, 400, "('temperature', 10), ('density', 0.5)")   
    """
)

cur.execute('SELECT row_set(additional_properties) AS result FROM materials')
results = cur.fetchall()
print(results)
