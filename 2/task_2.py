"""
Задание 2
Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH.
Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя свои
запросы и добавляя новые элементы, если потребуется.

"""
import os.path
from xml.etree import ElementTree as ET


"""
Скачал тестовый заказ в xml, практика работы с файлом
"""
tree = ET.parse(os.path.join("data", "order.xml"))
root = tree.getroot()

tags_list = list(root)

for tags in tags_list:
    print(f"\t{tags.tag}: {tags.text} {tags.attrib}")
    for child in tags:
        print(f"{child.tag}: {child.attrib} : {child.text}")



"""
Создание своей записи в xml
"""
root = ET.Element("record")
new_tag = ET.SubElement(root, "student")
new_tag.text = "Python Class"
print(ET.dump(root))


"""
Практика создания xml из заранее подготовленных данных
"""

data = [{"test x": x-40, "test y": x-10, "test z": x+20} for x in range(50, 60)]

root = ET.Element("database")

for item in data:
    record = ET.SubElement(root, "record")
    for key, value in item.items():
        key = key.replace(" ", "_")
        value = str(value).replace(" ", "_")
        element = ET.SubElement(record, key)
        element.text = str(value)

tree = ET.ElementTree(root)
tree.write(os.path.join("data", "test.xml"), encoding='utf-8')


"""
Практика с XPATH
"""

tree = ET.parse(os.path.join("data", "order.xml"))
root = tree.getroot()

names = root.findall("./Address/Name")
for name in names:
    print(
        name.tag,
        name.text,
        name.attrib
    )

items = root.findall("./Items/Item")
for item in items:
    print(
        item.tag,
        item.text,
        item.attrib
    )

prod = root.findall(".Items//Item/ProductName")
qty = root.findall("../Item/Quantity")
price = root.findall("../Item/USPrice")

for item in prod:
    print(item.tag, item.text)