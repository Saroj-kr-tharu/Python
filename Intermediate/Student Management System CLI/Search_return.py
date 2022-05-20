# Program to search a specfic element in the file
import json
from msvcrt import getch
from os import system
import GetData as getdata
import animator as animation


def SearchInReturn(name,filename="detail.json"):
    temp = getdata.ReturnData(filename)
    
    display = False
    no = 99
    for var in temp:
        for vale, keey in var.items():
            if vale == "Name":
                if keey.lower() == name.lower():
                    display = True
                    no = 1
                    ele=0
            if display == True:
                if ele==0:
                    str="\n\t\t\t <---- Sucessfully Found ----> "
                    animation.ReadingFromString(str)
                    ele=99
                
                if no <= 5:
                    str=(f"\n\t\t\t  {vale} -----> {keey} ")
                    animation.ReadingFromString(str)
                    no+=1

    if display==False:
        str=(f"\t\t    <---- Not Found {name} in the list ----> ")
        animation.ReadingFromString(str)
        return False
    else:
        return True
# SearchingASpecificData()  # This is for testing purpose
# ch=SearchInReturn('Sarffoj')
# if ch==True:
#     print(f"\t\t YEs ")
# else:
#     print(f"\t\t no")
