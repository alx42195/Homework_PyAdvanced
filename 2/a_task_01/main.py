"""
Дополнительное задание
Задание 1
Создайте функцию, которая будет создавать CSV файл на основе данных, введенных
пользователем через консоль. Файл должен содержать следующие колонки: имена, фамилии,
даты рождений и город проживания. Реализовать возможности перезаписи данного файла,
добавления новых строк в существующий файл, построчного чтения из файла и конвертацию
всего содержимого в форматы XML и JSON.
"""

from constructor import MakeCSV, json_convert, xml_convert

def main():
    """
    Function performs:
    1 - creation of CSV file from the user input
    2 - adding records to existing CSV file
    3 - converstion of created CSV file into JSON format
    4 - conversion into XML format, replacing spaces by "_", where needed

    it uses classes and functions from constructor module
    :return: dictionary in csv, json, xml
    """
    while True:
        reply = int(input("Select action: 1 - create CSV, 2 - add data to existing CSV, 3 - csv to json, 4 - csv to xml, 5 - quit > "))
        if reply == 5:
            break
        elif reply == 1:
            data = {
                "first_name": input("Enter first name > "),
                "last_name": input("Enter last name > "),
                "year_of_birth": input("Enter year of birth > "),
                "city_of_origin": input("Enter city of birth > "),
            }
            csv_file = MakeCSV(**data)
            csv_file.make_csv()
        elif reply == 2:
            data = {
                "first_name": input("Enter first name > "),
                "last_name": input("Enter last name > "),
                "year_of_birth": input("Enter year of birth > "),
                "city_of_origin": input("Enter city of birth > "),
            }
            csv_file = MakeCSV(**data)
            csv_file.add_csv()
        elif reply == 3:
            json_convert()
        elif reply == 4:
            xml_convert()
        elif reply == 5:
            break
        else:
            print("Wrong option, please try again!")
            continue

if __name__ == "__main__":
    main()
