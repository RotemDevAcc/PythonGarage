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



def RunProgram():
    ClearConsole()
    PrintActions()
    while True:
        user_action =input("Select Your Action: ")
        if user_action == None or user_action == "":
            print("No Action Selected")
            continue
        user_action =  Actions(int(user_action))

        if user_action == Actions.ADD:
            ManageAdding(Carslist)

        if user_action == Actions.DELETE:
            if len(Carslist) <= 0:
                print("Warning: Carlist is Empty, Please Add Cars Before Trying To Remove.")
                continue

            ManageDeletion(Carslist)

        if user_action == Actions.PRINT:
            if len(Carslist) <= 0:
                print("No Cars Found")
                continue

            for car in Carslist:
                print(f"Car Name: {car['name']}, Car Color: {car['color']}, Car Company: {car['company']}, Car Price: ${AddCommas(int(car['price']))}\n")


        if user_action == Actions.FIND:
            carname = input("Car Name: ")
            found,foundcar = findCarByName(Carslist,carname)
            if(found): print(f"Car Name: {foundcar['name']}, Car Color: {foundcar['color']}, Car Company: {foundcar['company']}, Car Price: ${AddCommas(int(foundcar['price']))}\n")
            else: print("Car " + carname + " Not Found")
        if user_action == Actions.CLOSE:
            print("Stopping Program")
            break

        if user_action == Actions.CLEARCONSOLE:
            ClearConsole()

def PrintActions():
    for action in Actions:
        print(f"{action.name} - {action.value}")

if __name__ == "__main__":
    Carslist = LoadCarsFromCSV()
    RunProgram()

