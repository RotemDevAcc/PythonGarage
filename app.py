from functions import *
from enum import Enum


Carslist = []

class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    FIND = 4
    CLOSE = 5
    CLEARCONSOLE = 6


# מתחיל את התהליך
def RunProgram():
    ClearConsole() # מנקה את הקונסול
    PrintActions() # מדפיס את כל הפעולות האפשריות שיש לנו
    while True:
        user_action =input("Select Your Action: ") # מבקש ממכם לבחור פעולה
        if user_action == None or user_action == "": # אם אין פעולה מתחילים מחדש כדי למנוע תקלות
            print("No Action Selected")
            continue
        user_action =  Actions(int(user_action))

        if user_action == Actions.ADD:
            ManageAdding(Carslist) # תהליך הוספת רכבים

        if user_action == Actions.DELETE:
            if len(Carslist) <= 0: # אם אין רכבים שמורים אין מה לעבור את התהליך הזה
                print("Warning: Carlist is Empty, Please Add Cars Before Trying To Remove.")
                continue

            ManageDeletion(Carslist) # תהליך מחיקת רכבים

        if user_action == Actions.PRINT:
            if len(Carslist) <= 0: # אם אין רכבים שמורים אין מה לעבור את התהליך הזה
                print("No Cars Found")
                continue
            # עובר על כל המערך של הרכבים ומדפיס שם, צבע, חברה, מחיר עם פסיקים, ואז יורד שורה לקראת הרכב הבא
            for car in Carslist:
                print(f"Car Name: {car['name']}, Car Color: {car['color']}, Car Company: {car['company']}, Car Price: ${AddCommas(int(car['price']))}\n")

            print("Total Cars: " + len(Carslist)) # סך הכל מכוניות


        if user_action == Actions.FIND:
            carname = input("Car Name: ")
            found,foundcar = findCarByName(Carslist,carname) # מחפש רכב על פי השם שלו
            if(found): print(f"Car Name: {foundcar['name']}, Car Color: {foundcar['color']}, Car Company: {foundcar['company']}, Car Price: ${AddCommas(int(foundcar['price']))}\n")
            else: print("Car " + carname + " Not Found")
        if user_action == Actions.CLOSE:
            print("Stopping Program")
            break # עוצר הכל

        if user_action == Actions.CLEARCONSOLE:
            ClearConsole() # מנקה את הקונסול

def PrintActions():
    for action in Actions:
        print(f"{action.name} - {action.value}")

if __name__ == "__main__": # כשהתוכנה עולה
    Carslist = LoadCarsFromCSV() # לבקש רכבים מהקובץ אם יש
    RunProgram() # מתחיל את כל התהליך

