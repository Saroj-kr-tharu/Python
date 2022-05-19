# Program to search a specfic element in the file
import json
from msvcrt import getch
from os import system


# import reading

def Deleting_Particular_Data(filename="detail.json"):

    display = []
    element = 0
    total_no_user=[]
    name = input("\t\t Enter Name To Search ----> ")
    with open(filename, 'r') as file:
        for var in file:
            element += 1
            dic = json.loads(var)
            for vale, kess in dic.items():
                if vale == "Name":
                    if name.lower() == kess.lower():
                        display.append(element)
            total_no_user.append(element)
    file.close()
    total_no_to_delete=len(display)
    total_no_in_database=len(total_no_user)
    print(f"\t\t\t Total Number Of User ----> {total_no_to_delete} ")
    print(f"\t\t\t Total Number Of User ----> {total_no_in_database} ")
    element = 0
    i=0
    delete_value = False
    new_data = {}
    new_data_list = []
    with open(filename, 'r') as file:
        for var in file:
            element += 1
            
            dic = json.loads(var)
            for vale, kess in dic.items():
                if element in display:
                    delete_value = True
                else:
                    with open("temp.json", 'a') as new_file:
                        json.dump(kess, new_file)
                        new_file.write("\n")
                        new_file.close()

            print("\n")
    file.close()


    note = ["Name", "Address", "Age", "Class", "Roll no"]
    i = 0
    display_to_be=total_no_in_database-total_no_to_delete
    element=1
    with open("temp.json", 'r') as file:
        for var in file:
            if element <= display_to_be:
                if i == 5:
                    print(f"\n")
                    i = 0
                    element+=1
                dic = json.loads(var)
                print(f"\t\t {note[i]} -----> {dic} ")
                i += 1
            else:
                return
    file.close()


Deleting_Particular_Data()  # This is for testing purpose
