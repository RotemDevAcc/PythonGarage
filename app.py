from functions import *
from enum import Enum


Carslist = []

class Actions(Enum):
    ADD = 1
    DELETE = 2
    PRINT = 3
    FIND = 4
    CLOSE = 5
    CLEAR = 6



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
            print(Carslist)

        if user_action == Actions.FIND:
            carname = input("Car Name: ")
            findCarByName(Carslist,carname)

        if user_action == Actions.CLOSE:
            print("Stopping Program")
            break

        if user_action == Actions.CLEAR:
            ClearConsole()

def PrintActions():
    for action in Actions:
        print(f"{action.name} - {action.value}")

if __name__ == "__main__":
    Carslist = LoadCarsFromCSV()
    RunProgram()

