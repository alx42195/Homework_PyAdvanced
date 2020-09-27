"""
Задание 3
Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов.
Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом.
"""

import csv
import os.path


class WeirdDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "!"
    delimiter = "~"
    lineterminator = "\n"

csv.register_dialect("strange_dialect", WeirdDialect)

with open(os.path.join("data", "item_short.csv")) as rfile:
    r = csv.reader(rfile)
    with open(os.path.join("data", "new_item_short.csv"), "w") as wfile:
        w = csv.writer(wfile, dialect="strange_dialect")
        for row in r:
            w.writerow(row)

sniff = csv.Sniffer()
sniffed_dialect = None

with open(os.path.join("data", "new_item_short.csv")) as readfile:
    r = csv.reader(readfile)
    for row in r:
        print(row)

with open(os.path.join("data", "new_item_short.csv")) as readfile:
    test = readfile.read()
    sniffed_dialect = sniff.sniff(test)

with open(os.path.join("data", "new_item_short.csv")) as readfile:
    r = csv.DictReader(readfile, dialect=sniffed_dialect)
    for row in r:
        print(row['Item ID'], row['Model'])


