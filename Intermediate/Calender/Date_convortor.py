# program to convert date 
from calendar import month
from msvcrt import getch
from os import system
import datetime
from nepali_date import NepaliDate

import animator as animation
class Convertor_date:
          

    def English_to_Nepali(self):
        """ English to Nepali date """
        try:
            years,months,days=input(" Enter date format like years/month/day ----> ").split("/")
            years=int(years)
            months=int(months)
            days=int(days)
        except:
            str=(f"\t\t <------  Invalid input ------>\n\t\t <---- Please enter valid input -----> ")
            animation.ReadingFromString(str)
            getch()
            system("cls")
            self.English_to_Nepali()
        my_birthday_in_ad=datetime.date(years,months,days)
        my_birthday_in_bs = NepaliDate.to_nepali_date(my_birthday_in_ad)

        print(f"\t\t In English date ----> {years}/{months}/{days} ")
        print(f"\t\t In Nepali date ----> {my_birthday_in_bs} ")
        # print(f" Nepali Date ---> { NepaliDate.to_nepali_date(my_birthday_in_ad) }")
        
    def Nepali_to_English(self):
        pass


cd=Convertor_date()
cd.English_to_Nepali()