
from msvcrt import getch
from os import system
import json

def Input_From_User():
    system("cls")
    # details = []
    main_details=[] # list of information
    details={}
    print(f"\t\t <---- Welcome to input section -----> ")
    name = input("\t\t Enter name     ----->")
    address = input("\t\t Enter Address ----->")
    age = input("\t\t Enter Age    ----->")
    clas = input("\t\t Enter Class  ----->")
    roll = input("\t\t Enter Roll no  ----->")
   
    details["Name"]=name
    details["Address"]=address
    details["Age"]=age
    details["Class"]=clas
    details["Roll no "]=roll
    return details

def Writing_To_Disk(filename="detail.json",mode='a'):
    try:
        with open(filename, mode) as file:
            json.dump(Input_From_User(), file)
            file.write("\n")
        file.close()

    except:
        print(f"\t\t <---- File opening error ----> ")
    else:
        print(f"\t\t <---- Sucessfully written to file  ---> ")
        
Writing_To_Disk()
