import os
import csv
filename = "cars.csv"

# מנקה קונסול
def ClearConsole():
    os.system("cls" if os.name == "nt" else "clear")


# מוסיף פסיקים למספר במקום 1000 אז יהיה 1,000 ויותר מובן
def AddCommas(number):
    return ("{:,}".format(number))


# תהליך מחיקת רכבים
def ManageDeletion(table):
    carname = input("Enter Car Name: ") # שם רכב

    found,car = findCarByName(table,carname) # למצוא רכב על פי השם
    if not found: # הרכב לא נמצא
        print(f"\033[93m{carname} Not Found In Database\033[0m")
    else: # הרכב נמצא
        print(f"{car['name']} Deleted")
        # מוחק את הרכב מהמערך
        table.remove(car)
        # מעדכן את השינויים לקובץ
        SaveCarsToCSV(table)


#תהליך הוספת רכבים
def ManageAdding(table):


    carname = input("Enter Car Name [Example: Land Cruiser]: ")
    carcolor = input("Enter Car Color [Example: Baby Blue]: ")
    carcomp = input("Enter Car Type [Example: BMW, Audi]: ")
    carprice = input("Enter Car Price [Numbers Only]: ")



    # אם המחיר לא יכול להיות מספיר עוצרים ומדווחים
    if not carprice.strip().isdigit():
        return print("\033[93mERROR: Car Price Must Be An Integer (Number)\033[0m")

    # אם מילאנו את כל הפרטים
    if(carname and carcolor and carcomp and carprice):
        # מוסיפים למערך
        table.append({"name" : carname, "color" : carcolor, "company": carcomp, "price": carprice})
        # שומרים לקובץ
        SaveCarsToCSV(table)
        # מדפיסים שם, צבע, חברה, ומחיר
        print(f"Added A New Car, Name: {carname}\nColor: {carcolor}\nCompany: {carcomp}\nPrice: ${AddCommas(int(carprice))}")
    else: # אם לא
        print(f"\033[93mError: Not Enough Arguments Wanted 4 Got Less\033[0m")



# מחפש משהו במערך על פי שם לא חייב להיות מכוניות
def findCarByName(table,name):
    for car in table:
        if car["name"] == name:
            return True,car
        
    return None,None


# שומר את הפרטים לקובץ
def SaveCarsToCSV(table):
    # משתמשם בשם קובץ שמוגדר למעלה
    global filename 
    # CSV פותח את הקובץ עם גישת כתיבה בתור קובץ
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'color', 'company', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for car in table:
            writer.writerow(car)
    print(f'Carslist saved to {filename}')


# טוען את הרכבים השמורים
def LoadCarsFromCSV():
    # משתמשם בשם קובץ שמוגדר למעלה
    global filename 
    table = []
    # מנסה לפתוח את הקובץ
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
     # אם לא נמצא
    except FileNotFoundError:
        print(f'File not found: {filename}')
        # מחזיר מערך ריק
        return [] 
    # כל בעיה אחרת שלא הצליח לפתוח בגללה
    except Exception as e: 
        # מחזיר מערך ריק
        return [] 