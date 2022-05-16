
from msvcrt import getch
from os import system
from random import randint, random


def roll_the_dice():

        choice=randint(1,6)
        choice=randint(1,6)
        print(f"\t\t Dice ----> {choice} ")
        getch()
  


def menu():
    """ This is menu function """
    while True:
        system("cls")
        system("color 2a")
        print("\t\t <-----------------------------------------------> ")
        print(f"\t\t <-------- Welcome to Roll The dice program --->")
        print(f"\t\t     <------ 1. Roll The dice --->")
        print(f"\t\t     <------ 99. exit   --------->")
        print("\t\t <-----------------------------------------------> ")
        ch=int(input())

        if ch==1:
            roll_the_dice()
        elif ch==99:
            print(f"\t\t <----- Thanks for using our program -----> ")
            exit()
        else:
            print("\t\t <---- Invalid options ---->")

# menu 
menu()