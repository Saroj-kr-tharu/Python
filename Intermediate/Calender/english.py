# Program to print the English Date
import datetime
import calendar
from msvcrt import getch
from os import system

import animator as animation

# global month,year


def menu():
    """ Main menu of the english calendar """
    """ This is Only Menu Section """
    banner = "art/banner.txt"
    while True:
        system("cls")
        animation.ReadingFromFile(banner, 8)
        str = (f"\n\t\t <------ Welcome to English Calendar  -------> ")
        animation.ReadingFromString(str)
        print(f"\n\t\t   <------ 1.  Current Year  ------> ")
        print(f"\t\t   <------ 2.  Search Date   ------> ")
        print(f"\t\t   <------ 5.  Current Date  ------> ")
        print(f"\t\t   <------ 10. Return Main Menu  ------> ")
        str = (f"\t\t <-------------------------------------------> ")
        animation.ReadingFromString(str)
        try:
            ch = int(input())
        except:
            str = (f"\t\t <---- Please enter a valid options  ---> \n")
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
            current_date()
        elif ch == 10:
            print(f"\n\t\t <----- Returning To Main Menu  ------>")            
            break
        else:
            str = (f"\n\t\t <---- Invalid Options ----> ")
            animation.ReadingFromString(str)


def current_date():
    today = datetime.date.today()
    d2 = today.strftime("%B %d, %Y")

    str = (f"\n\n\t\t\t <----- Current date ----> ")
    animation.ReadingFromString(str)
    str = (f"\n\t\t\t <----- {today}  ------>")
    animation.ReadingFromString(str)
    str = (f"\n\t\t\t <----- {d2}  ------>")
    animation.ReadingFromString(str)
    getch()


def search_specific_date(specific_value=True, month=1, year=2022):
    """ Its Print the Specfic month of the years  """
    weeK_user = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    if specific_value == True:
        try:
            year = int(input("\n\t\t Enter Years ----> "))
            month = int(input("\t\t Enter month ----> "))
        except:
            print(f"\t\t<---- Please Enter valid input ---->")
            getch()
            search_specific_date()

    system("cls")

    chi = month
    chi = str(chi)
    datetime_object = datetime.datetime.strptime(chi, "%m")
    month_name = datetime_object.strftime("%B")
    print(f"\n\t\t\t\t  {month_name} {year} ")
    print(f"\t\t", end='')
    for var in weeK_user:
        print(f"   {var} ", end="")
    cal = calendar.monthcalendar(year, month)
    for var in cal:

        print(f"\n\t\t", end="")
        for car in var:
            if car == 0:
                mar = "  "
                print(f"   {mar}  ", end="")
            elif car < 10:
                mar = f" {car}"
                print(f"   {mar}  ", end="")
            else:
                print(f"   {car}  ", end="")
    print(f"\n")
    event_checking(month, year)


def whole_year_month():
    system("cls")
    print(f"{calendar.calendar(2022)}")


def event_checking(month, year):
    str = (f"\n\t\t  <----- N For Next Month ------>")
    animation.ReadingFromString(str)
    str = (f"\n\t\t  <----- Y For Next Year ------>")
    animation.ReadingFromString(str)
    str = (f"\n\t\t  <----- q For Return Main Menu ------>")
    animation.ReadingFromString(str)
    try:
        ch = input()
    except:
        str = (f"\n\t\t <---- Please enter a valid options  ---> ")
        animation.ReadingFromString(str)
        getch()
        menu()

    if ch == 'N' or ch == 'n':
        if month == 12:
            month = 0

        specific_value = False
        month += 1
        search_specific_date(specific_value, month, year)

    elif ch == 'Y' or ch == 'y':

        specific_value = False
        year += 1
        search_specific_date(specific_value, month, year)
        pass
    elif ch == 'q' or ch == 'Q':
        print(f"\n\t\t <--- Returning to main menu ----> ")
        specific_value = True
        menu()

    else:
        print(f"\n\t\t <--- Invalid Options ----> ")  
        getch()
        specific_value = False
        search_specific_date(specific_value, month, year)


# eg = English_Calendar()
# eg.current_date()
# # eg.search_specific_date()
# menu()
