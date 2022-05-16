# program to manage Student

from msvcrt import getch
from os import system
import json


def inputing():
    system("cls")
    details = []
    print(f"\t\t <---- Welcome to input section -----> ")
    name = input("\t\t Enter name     ----->")
    address = input("\t\t Enter Address ----->")
    age = input("\t\t Enter Age    ----->")
    clas = input("\t\t Enter Class  ----->")
    roll = input("\t\t Enter Roll no  ----->")
    details.append(name)
    details.append(address)
    details.append(age)
    details.append(clas)
    details.append(roll)
   
    with open("detail.json", "a") as file:
        json.dump(details, file)
        file.write("\n")
    file.close()
    print(f"\t\t <---- Sucessfully written to file  ---> ")
    getch()

def display():
    
    print(f"\t\t <----- Welcome to Display section -----> ")
    with open("detail.json", 'r') as file:
        for var in file:
            print(var)
    #         red = json.load(var)
    # file.close()
    # print(f"\t\t <----------------------------------->")
    # print(f"\t\t Name -----> {red[0]} ")
    # print(f"\t\t Address -----> {red[1]} ")
    # print(f"\t\t Age -----> {red[2]} ")
    # print(f"\t\t Class -----> {red[3]} ")
    # print(f"\t\t Roll no  -----> {red[4]} ")
    # print(f"\t\t <----------------------------------->")
    getch()

def menu():
    while True:
        system("cls")
        system("color 2a")
        print("\t\t<----------------------------------------->")
        print(f"\t\t<------ 1 . Input   ----->")
        print(f"\t\t<------ 2 . Display ----->")
        print(f"\t\t<------ 3 . Destory ----->")
        print(f"\t\t<------ 5 . display ----->")
        print(f"\t\t<------ 99. Input   ----->")
        print("\t\t<----------------------------------------->")
        ch = int(input())
        if ch == 1:
            inputing()
        elif ch == 2:
            display()
        elif ch == 3:
            # display()
            k=0
        elif ch == 5:
            # display()
            k=0
        elif ch == 99:
            print(f"\t\t <----- Thanks for using our program -----> ")
            exit()
        else:
            print("\t\t <----- Invalid options -----> ")
        getch()

menu()
