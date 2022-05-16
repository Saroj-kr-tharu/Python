
from msvcrt import getch
from os import system
from random import randint, random


def guess_nbr():
    num = int(input("\t\t Enter intial range ----> "))
    num1 = int(input("\t\t Enter Final range ----> "))
    try:
        choice = randint(num, num1)

    except:
        system("cls")
        print(f"\t\t {num} Intial is less than {num1} Final ")
        print(f"\t\t <---- Please enter a valid number ----> ")
        guess_nbr()
    else:
        life = 1
        while True:
            if life <= 3:
                system("cls")
                choic = int(input("\t\t Enter Your Guess Number ----> "))

                if choic <= num1 and choic  >=num:
                    life=life
                else:
                    print(f"\t\t<--- {choic} is not in range of {num} to {num1} ---->")
                    
                if choice == choic:
                    print(
                        f"\t\t <--- Congratulation you guess number in {life} attemp")
                    print(f"\t\t<----  Winner winner Chicken dinner ----> ")
                    
                    break
                else:
                    print(f"\t\t <--- Ops you guess number {choic} is not matched ---> ")
                    if choice<choic:
                        print(f"\t\t <---- {choic} is greater than  Exact number -----> ")
                    elif choice > choic:
                        print(f"\t\t <---- {choic} is lesser than  Exact number -----> ")
                        
                    print(f"\t\t <------- Your life remains {3-life} ----->")
                    getch()
                life += 1
            else:
                system("cls")
                print(f"\t\t <----- Sorry you  have  {life-1} lifeline is finished ----> ")
                print(f"\t\t <----- Exact number is  {choice} ----> ")
                print(f"\t\t <---- Returing to main menu ----> ")
                break

    getch()


def menu():
    """ This is menu function """
    while True:
        system("cls")
        system("color 2a")
        print("\t\t <-----------------------------------------------> ")
        print(f"\t\t <---- Welcome to Guess The Number  program --->")
        print(f"\t\t     <------ 1. Guess The Number  --->")
        print(f"\t\t     <------ 99. exit   --------->")
        print("\t\t <-----------------------------------------------> ")
        ch = int(input())

        if ch == 1:
            guess_nbr()
        elif ch == 99:
            print(f"\t\t <----- Thanks for using our program -----> ")
            exit()
        else:
            print("\t\t <---- Invalid options ---->")
    getch()

# menu
menu()
