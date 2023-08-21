import os
import csv
filename = "cars.csv"
def ClearConsole():
    os.system("cls" if os.name == "nt" else "clear")


def AddCommas(number):
    return ("{:,}".format(number))

def ManageDeletion(table):
    carname = input("Enter Car Name: ")

    found,car = findCarByName(table,carname)
    if not found:
        print(f"{carname} Not Found In Database")
    else:
        print(f"{car['name']} Deleted")
        table.remove(car)
        SaveCarsToCSV(table)


def ManageAdding(table):
    carname = input("Enter Car Name [Example: Land Cruiser]: ")
    carcolor = input("Enter Car Color [Example: Baby Blue]: ")
    carcomp = input("Enter Car Type [Example: BMW, Audi]: ")
    carprice = input("Enter Car Price [Numbers Only]: ")



    if not carprice.strip().isdigit():
        return print("ERROR: Car Price Must Be An Integer (Number)")

    if(carname and carcolor and carcomp and carprice):
        table.append({"name" : carname, "color" : carcolor, "company": carcomp, "price": carprice})
        SaveCarsToCSV(table)
        print(f"Added A New Car, Name: {carname}\nColor: {carcolor}\nCompany: {carcomp}\nPrice: {AddCommas(int(carprice))}")
    else:
        print(f"Error: Not Enough Arguments Wanted 4 Got Less")

def is_number(value):
    return isinstance(value, (int, float))

def findCarByName(table,name):
    for car in table:
        if car["name"] == name:
            return True,car
        
    return None,None


def SaveCarsToCSV(table):
    global filename
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'color', 'company', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for car in table:
            writer.writerow(car)
    print(f'Carslist saved to {filename}')


def LoadCarsFromCSV():
    global filename
    table = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                table.append({
                    'name': row['name'],
                    'color': row['color'],
                    'company': row['company'],
                    'price': row['price']
                })
        print(f'Carslist loaded from {filename}')
        return table
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return []
    except Exception as e:
        return []