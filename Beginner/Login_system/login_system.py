# Program to login in system
from msvcrt import getch
from os import system
import time

import CreateAccout as CA
import Login_Account as LA
import Destory_Database as DB
import animator as animation

def intial():
    system("color a")
    welcome="art/Art.txt"
    developer="art/Developer.txt"
    system("cls")
    animation.ReadingFromFile(welcome,99)
    animation.ReadingFromFile(developer,5)
    time.sleep(2)
    system("cls")

def menu():
    banner="art/banner.txt"
    while True:
        system("cls")
        animation.ReadingFromFile(banner,4)
        print(f"\n\t\t\t   <-------  Welcome to Main Menu   ------>")
        print(f"\t\t\t   <------------------------------------->")
        print(f"\t\t\t   <--------- 1.  Create Account -------->")
        print(f"\t\t\t   <--------- 2.  Login Account  -------->")
        print(f"\t\t\t   <--------- 5.  About          -------->")
        print(f"\t\t\t   <--------- 10. Destory Database   ---->")
        print(f"\t\t\t   <--------- 99. Exit       ------------>")
        print(f"\t\t\t   <------------------------------------->")
        ch=int(input())
        if ch==1:
            system("cls")
            animation.ReadingFromFile(banner,4)
            CA.CreateAccount()
        elif ch==2:
            system("cls")
            animation.ReadingFromFile(banner,4)
            LA.Login_Account()
        elif ch==10:
            system("cls")
            animation.ReadingFromFile(banner,4)
            DB.DestoryDataBase()
        elif ch==5:
            system("cls")
            animation.ReadingFromFile("art/Developer.txt")
        elif ch==99:
            thank="\t\t <----- Thanks For Using Our Program -----> \n\t\t   <------- Quiting ------>"
            animation.ReadingFromString(thank,0.02)
            exit()
        else:
            print(f"\t\t <----- Invalid options ----->")
        getch()

intial()
menu()