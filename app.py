from functions import *
from enum import Enum


Carslist = {}

class Actions(Enum):
    ADD = 1
    DELETE = 2
    UPDATE = 3
    PRINT = 4
    FIND = 5
    CLOSE = 6
    CLEARCONSOLE = 7


# מתחיל את התהליך
def RunProgram():
    # מנקה את הקונסול
    ClearConsole() 
    # מדפיס את כל הפעולות האפשריות שיש לנו
    PrintActions() 
    while True:
        # מבקש ממכם לבחור פעולה
        user_action =input("Select Your Action: ") 
        # אם אין פעולה מתחילים מחדש כדי למנוע תקלות
        if user_action == None or user_action == "": 
            print("\033[93mNo Action Selected\033[0m")
            continue
        user_action =  Actions(int(user_action))

        if user_action == Actions.ADD:
            # תהליך הוספת רכבים
            ManageAdding(Carslist) 

        if user_action == Actions.DELETE:
             # אם אין רכבים שמורים אין מה לעבור את התהליך הזה
            if len(Carslist) <= 0:
                print("\033[93mWarning: Carlist is Empty, Please Add Cars Before Trying To Remove.\033[0m")
                continue

            ManageDeletion(Carslist) # תהליך מחיקת רכבים

        if user_action == Actions.UPDATE:
            UpdateCars(Carslist)

        if user_action == Actions.PRINT:
            # אם אין רכבים שמורים אין מה לעבור את התהליך הזה
            if len(Carslist) <= 0: 
                print("No Cars Found")
                continue
            # עובר על כל המערך של הרכבים ומדפיס שם, צבע, חברה, מחיר עם פסיקים, ואז יורד שורה לקראת הרכב הבא
            for car in Carslist:
                print(f"Car Name: {car['name']}, Car Color: {car['color']}, Car Company: {car['company']}, Car Price: \033[92m${AddCommas(int(car['price']))}\n\033[0m")
            # סך הכל מכוניות
            print(f"\033[92mTotal Cars: {len(Carslist)}\033[0m") 


        if user_action == Actions.FIND:
            carname = input("Car Name: ")
            # מחפש רכב על פי השם שלו
            found,foundcar = findCarByName(Carslist,carname) 
            if(found): print(f"\033[92mCar Name: {foundcar['name']}, Car Color: {foundcar['color']}, Car Company: {foundcar['company']}, Car Price: ${AddCommas(int(foundcar['price']))}\n\033[0m")
            else: print("Car " + carname + " Not Found")
        if user_action == Actions.CLOSE:
            print("\033[93mStopping Program\033[0m")
            # עוצר הכל
            break 

        if user_action == Actions.CLEARCONSOLE:
            # מנקה את הקונסול
            ClearConsole() 

def PrintActions():
    for action in Actions:
        print(f"\033[95m{action.name} - {action.value}\033[0m")


# כשהתוכנה עולה
if __name__ == "__main__": 
    # לבקש רכבים מהקובץ אם יש
    Carslist = LoadCarsFromCSV()
    # מתחיל את כל התהליך
    RunProgram() 

