# Program to print the English Date
import datetime
import nepali_datetime
import nepali_date
import calendar
from msvcrt import getch
from os import system
import animator as animation


def menu():
    """ This is Only Menu Section """
    banner = "art/banner.txt"
    while True:
        system("cls")
        animation.ReadingFromFile(banner, 8)
        str = (f"\n\t\t <------ Welcome to Nepali Calendar  -------> ")
        animation.ReadingFromString(str)
        print(f"\n\t\t     <------ 1.  Current Year  ------> ")
        print(f"\t\t     <------ 2.  Search Date   ------> ")
        print(f"\t\t     <------ 5.  Current Date  ------> ")
        print(f"\t\t     <------ 10. Return Main Menu  ------> ")
        str = (f"\t\t <-------------------------------------------> ")
        animation.ReadingFromString(str)
        try:
            ch = int(input())
        except:
            str=(f"\t\t <---- Please enter a valid options  ---> \n")
            animation.ReadingFromString(str)
            getch()
            menu()

        if ch == 1:
            system("cls")
            animation.ReadingFromFile(banner, 8)
            whole_year_month()
            getch()
        elif ch == 2:
            system("cls")
            animation.ReadingFromFile(banner, 8)
            search_specific_date()
            getch()
        elif ch == 5:
            system("cls")
            animation.ReadingFromFile(banner, 8)
            Current_date()
            getch()
        elif ch == 10:            
            print(f"\n\t\t <----- Returning To Main Menu  ------>")            
            break
        else:
            animation.ReadingFromFile(banner, 8)
            str = (f"\n\t\t <---- Invalid Options ----> ")
            animation.ReadingFromString(str)


def Current_date():
    str=(f"\n\t\t <----- Current Date -----> ")
    animation.ReadingFromString(str)
    str=(f"\n\t\t    {nepali_datetime.date.today() }")
    animation.ReadingFromString(str)
    


def search_specific_date(specific_value=True, year=2079, month=1):
    """ Its Print the Specfic month of the years  """
    if specific_value == True:
        try:
            year = int(input("\n\t\t Enter Years ----> "))
            month = int(input("\t\t Enter month ----> "))
        except:
            print(f"\t\t <---- Please enter a valid options  ---> ")
            print(f"\t\t <---- Returning ..  ---> ")
            getch()
            system("cls")
            search_specific_date()
    system("cls")
    nepali_datetime.date(year, month, 1).calendar(justify=15)
    event_checking(year, month)


def whole_year_month():
    system("cls")
    for i in range(1, 13):
        nepali_datetime.date(2079, i, 1).calendar(justify=6)
        # print(f"\n")


def event_checking(year, month):
    str=(f"\n\t\t  <----- N For Next Month ------>")
    animation.ReadingFromString(str)
    str=(f"\n\t\t  <----- Y For Next Year ------>")
    animation.ReadingFromString(str)
    str=(f"\n\t\t  <----- q For Return Main Menu ------>")
    animation.ReadingFromString(str)
    try:
        ch = input()
    except:
        print(f"\t\t <---- Please enter a valid options  ---> ")
        getch()
        system("cls")
        event_checking(year, month)
    if ch == 'N' or ch == 'n':
        if month == 12:
            month = 0
        specific_value = False
        month += 1
        search_specific_date(specific_value, year, month)
    elif ch == 'Y' or ch == 'y':
        specific_value = False
        year += 1
        search_specific_date(specific_value, year, month)
        pass
    elif ch == 'q' or ch == 'Q':
        print(f"\t\t <--- Returning to main menu ----> ")        
        getch()
        menu()
    else:
        print(f"\t\t <--- Invalid Options ----> ")        
        specific_value = False
        getch()
        search_specific_date(specific_value, year, month)


# eg = Nepali_Calendar()
# # eg.search_specific_date()
# menu()
# eg.search_specific_date()
# eg.whole_year_month()
# eg.Current_date()
