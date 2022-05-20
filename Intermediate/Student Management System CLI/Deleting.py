# Program to search a specfic element in the file
import json
from msvcrt import getch
import os
import animator as animation
import GetData as getdata


def Deleting_Particular_Data():
    temp = getdata.ReturnData()
    temp_data = {}

    display = False
    no = 99
    str=(f"\n\t\t <-------- Welcome To Delete Section --------> ")
    animation.ReadingFromString(str)

    str=("\n\t\t\t  Enter name to delete ---> ")
    animation.ReadingFromString(str)
    name=input()

    for var in temp:
        for vale, keey in var.items():
            if vale == "Name":
                if keey.lower() == name.lower():
                    display = True
                    no = 1
            if display == True:
                if no <= 5:
                    print(f"\t\t\t  {vale} -----> {keey} ")
                    temp_data[vale] = keey
                    no += 1

        print(f"\n", end='')

    try:
        temp.remove(temp_data)
    except:
        str=(f"\n\t\t   <---- {name} is not in list ----> ")
        animation.ReadingFromString(str)
        return

    # print(f"\n\t\t Final data ----> {temp} ")
    with open("temp.json", 'w') as file:
        json.dump(temp, file)
    file.close()

    os.remove("detail.json")
    os.rename("temp.json", "detail.json")
    str=(f"\t\t\t   <--- Sucessfully Delete ----> ")
    animation.ReadingFromString(str)


# Deleting_Particular_Data()  # This is for testing purpose
