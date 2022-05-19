# program to manage Student

from fileinput import filename
import os
from msvcrt import getch
from os import remove, system
import json
import Searching_in_File 
import Destroy_database as db
import reading as red
import inputing as inpu







def menu():
    while True:
        system("cls")
        system("color 2a")
        print("\t\t<----------------------------------------->")
        print(f"\t\t<------ 1 . Input   ----->")
        print(f"\t\t<------ 2 . Display ----->")
        print(f"\t\t<------ 3 . Destory ----->")
        print(f"\t\t<------ 5 . Search ----->")
        print(f"\t\t<------ 99. Exit   ----->")
        print("\t\t<----------------------------------------->")
        ch = int(input())
        if ch == 1:
            inputi()
        elif ch == 2:
            red.DisplayingToScreeenFromFile()
        elif ch == 3:
            db.DestoryingTheDatabase()
        elif ch == 5:
            Searching_in_File.sea()
        elif ch == 99:
            print(f"\t\t <----- Thanks for using our program -----> ")
            exit()
        else:
            print("\t\t <----- Invalid options -----> ")
        getch()

menu()
