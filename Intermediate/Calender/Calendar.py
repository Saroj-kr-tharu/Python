# Program to print the calender
from msvcrt import getch
from os import system
from time import sleep
# import english as eng
import NEPALI as nep
import english as eng
import animator as animation

class calender_main:
    def inital(self):
        system("cls")
        system("color a")
        developer="art/Developer.txt"
        welcome="art/Art.txt"

        animation.ReadingFromFile(welcome)
        animation.ReadingFromFile(developer,5)
        sleep(0.6)
        system("cls")

    def menu(self):
        """ This is Only Menu Section """
        # def __init__(self):
        # self.nepali=nep.Nepali_Calendar()
        # self.english=eng.English_Calendar()
        developer="art/Developer.txt"
        welcome="art/Art.txt"
        banner="art/banner.txt"
        while True:
            system("cls")
            self.inital()
            # print(f"\t\t <------ Welcome to Main Menu  -------> ")
            animation.ReadingFromFile(banner,88)
            str=(f"\n\t\t\t <------ Welcome to Main Menu  -------> ")
            animation.ReadingFromString(str)

            print(f"\n\t\t\t <------ 1.  English Calendar  ------> ")
            print(f"\t\t\t <------ 2.  Nepali  Calendar  ------> ")
            # print(f"\t\t <------ 3.  Date    Convertor ------> ")
            print(f"\t\t\t <------ 10. About   Calendar  ------> ")
            print(f"\t\t\t <------ 99.      Exit         ------> ")
            try:
                ch = int(input())
            except:
                str=(f"\t\t\t <---- Invalid options ----> \n\t\t\t <---- Please Reenter data ----> ")
                animation.ReadingFromString(str)
                getch()
                self.menu()

            if ch == 1:
                eng.menu()
            elif ch == 2:
                nep.menu()
            # elif ch == 3:
            #     pass
            elif ch == 10:
                system("cls")
                animation.ReadingFromFile(developer)
                getch()
            elif ch == 99:
                str=(f"\t\t <----- Thanks For Using Our Program ------>")
                animation.ReadingFromString(str)
                exit()
            else:
                str=(f"\t\t <---- Invalid Options ----> ")
                animation.ReadingFromString(str)


ca = calender_main()
ca.menu()
