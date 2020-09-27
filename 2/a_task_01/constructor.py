import csv
import json
from xml.etree import ElementTree as ET


class FineDialect(csv.Dialect):
    """
    Making our own dialect to be used for CSV file creation
    """
    quoting = csv.QUOTE_ALL
    quotechar = "'"
    delimiter = "|"
    lineterminator = "\n"


csv.register_dialect("weird", FineDialect)


class MakeCSV:
    def __init__(self, first_name: dict, last_name: dict, year_of_birth: dict, city_of_origin: dict):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.city_of_origin = city_of_origin

    def make_csv(self):
        """
        Function creates CSV file based on user input.
        Dialect "weird" is used
        """
        with open("data.csv", "w") as wfile:
            names = ["first name", "last name", "year of birth", "city of origin"]
            w = csv.DictWriter(wfile, fieldnames=names, dialect="weird")
            w.writeheader()
            w.writerow(
                {
                    "first name": self.first_name,
                    "last name": self.last_name,
                    "year of birth": self.year_of_birth,
                    "city of origin": self.city_of_origin,
                }
            )

    def add_csv(self):
        """
        Function adds records into existing CSV file.
        Dialect "weird" is used
        :return: csv file
        """
        with open("data.csv", "a") as wfile:
            names = ["first name", "last name", "year of birth", "city of origin"]
            w = csv.DictWriter(wfile, fieldnames=names, dialect="weird")
            w.writerow(
                {
                    "first name": self.first_name,
                    "last name": self.last_name,
                    "year of birth": self.year_of_birth,
                    "city of origin": self.city_of_origin,
                }
            )

def json_convert():
    """
    Function converts earlier created file into JSON format
    :return: JSON file
    """
    with open("data.csv") as rf:
        reader = csv.DictReader(rf, dialect="weird")
        content = [row for row in reader]
        with open("data.json", "w") as wfile:
            json.dump(content, wfile, indent=4)

def xml_convert():
    """
    Function prepares CSV file for conversion into XML by replacing " " with "_"
    Then the file is converted into XML
    :return: XML file
    """
    with open("data.csv") as rf:
        reader = csv.DictReader(rf, dialect="weird")
        content = [row for row in reader]
        root = ET.Element("persons")
        for item in content:
            record = ET.SubElement(root, "record")
            for key,value in item.items():
                key = key.replace(" ", "_")
                e = ET.SubElement(record,key)
                e.text = value
        tree = ET.ElementTree(root)
        tree.write("data.xml", 'utf-8')



