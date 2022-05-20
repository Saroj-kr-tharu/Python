# program to manage Student


import os
from msvcrt import getch

import json
from time import sleep
import Searching_in_File as searching
import Destroy_database as db
import reading as red
import inputing as inpu
import Deleting as dele
import Replace as rep
import animator as animation


def intial():
    os.system("cls")
    os.system("color 2a")
    developer="art/Developer.txt"
    welcome="art/Art.txt"

    animation.ReadingFromFile(welcome)
    animation.ReadingFromFile(developer,5)
    sleep(0.6)
    os.system("cls")


def menu():
    developer="art/Developer.txt"
    welcome="art/Art.txt"
    banner="art/banner.txt"
    while True:
        os.system("cls")
        animation.ReadingFromFile(welcome,4)

        str="\n\t\t\t      <-------- Welcome To Main Menu --------------->"
        animation.ReadingFromString(str)
        print("\n\t\t\t\t <----------------------------------->")
        print(f"\t\t\t\t   <------ 1 . Input   ----->")
        print(f"\t\t\t\t   <------ 2 . Display ----->")
        print(f"\t\t\t\t   <------ 3 . Destory ----->")
        print(f"\t\t\t\t   <------ 4 . Delete ----->")
        print(f"\t\t\t\t   <------ 5 . Search ----->")
        print(f"\t\t\t\t   <-----  6 . Replace ----->")
        print(f"\t\t\t\t   <-----  10. About   ----->")
        print(f"\t\t\t\t   <------ 99. Exit   ----->")
        print("\t\t\t\t<----------------------------------->")
        ch = int(input())
        if ch == 1:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            inpu.Writing_To_Disk()
            getch()
        elif ch == 2:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            red.DisplayingToScreeenFromFile()
            getch()
        elif ch == 3:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            db.DestoryingTheDatabase()
            getch()
        elif ch == 4:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            dele.Deleting_Particular_Data()
            getch()
        elif ch == 5:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            searching.SearchingASpecificData()
        elif ch == 6:
            os.system("cls")
            animation.ReadingFromFile(banner,8)
            rep.ReplaceAParticular()
            getch()
        elif ch == 10:
            os.system("cls")
            animation.ReadingFromFile(developer)
            getch()
        elif ch == 99:
            str=(f"\t\t <----- Thanks for using our program -----> ")
            animation.ReadingFromString(str)
            exit()
        else:
            str=("\t\t <----- Invalid options -----> ")
            animation.ReadingFromString(str)
        getch()

# intial()
menu()
