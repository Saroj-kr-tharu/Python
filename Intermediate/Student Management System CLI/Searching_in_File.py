# Program to search a specfic element in the file
import json
from msvcrt import getch
from os import system


# import reading

def sea(filename="detail.json"):

    display = []
    element = 0
    name = input("\t\t Enter Name To Search ----> ")
    with open(filename, 'r') as file:
        for var in file:
            element += 1
            dic = json.loads(var)
            for vale, kess in dic.items():
                if vale == "Name":
                    if name.lower() == kess.lower():
                        display.append(element)
    file.close()
    print(f"\t\t\t Total Number Of User ----> {len(display)} ")
    element = 0
    with open(filename, 'r') as file:
        for var in file:
            element += 1
            dic = json.loads(var)
            for vale, kess in dic.items():
                if element in display:
                    print(f"\t\t {vale} -----> {kess} ")
            print("\n")
    file.close()


sea()  # This is for testing purpose
