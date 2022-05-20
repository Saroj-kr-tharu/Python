import json
import os
import GetData as getdata
import inputing as inpt
import animator as animation

def ReplaceAParticular():
    str=(f"\t\t <-------- Welcome To Replace Section -------> \n")
    animation.ReadingFromString(str)
    
    temp = getdata.ReturnData()
    str=("\t\t\t  Enter name to replace ---> ")
    animation.ReadingFromString(str)
    name=input()

    display = False
    no = 99
    num = 99
    element = 0
    for var in temp:
        element += 1
        for vale, kess in var.items():
            if vale == "Name":
                if kess.lower() == name.lower():
                    display = True
                    no = 1
            if display == True:
                if no <= 5:
                    print(f"\t\t\t  {vale} ---> {kess} ")
                    no += 1
                    num = element
    print(f"\n", end='')

    if display == True:
        str=(f"\t\t\t  Element ---> {num-1} ")
        animation.ReadingFromString(str)

        data = inpt.Input_From_User(88)
        temp[num-1] = data
        with open("detail.json", 'w') as file:
            json.dump(temp, file)
        file.close()
        str=(f"\t\t <---  Sucessfully Replace at index {num -1} --->")
        animation.ReadingFromString(str)
    


    else:
        str=(f"\t\t   <--- {name} is not founded in list ----> ")
        animation.ReadingFromString(str)


    

# ReplaceAParticular()
