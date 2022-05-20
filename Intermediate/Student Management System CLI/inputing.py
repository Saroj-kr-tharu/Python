
import json
import GetData as getdata
import animator as animation

def Input_From_User(mod=99):
    # mode = 99 means add 
    details = {}
    
    str=(f"\n\t\t <---- Welcome to input section -----> ")
    animation.ReadingFromString(str)

    str = ("\n\t\t\t  Enter name     ----->")
    animation.ReadingFromString(str,0)
    name=input()

    str = ("\t\t\t  Enter Address ----->")
    animation.ReadingFromString(str)
    address=input()

    str = ("\t\t\t  Enter Age    ----->")
    animation.ReadingFromString(str)
    age=input()

    str = ("\t\t\t  Enter Class  ----->")
    animation.ReadingFromString(str)
    clas=input()

    str = ("\t\t\t  Enter Roll no  ----->")
    animation.ReadingFromString(str)
    roll=input()

    details["Name"] = name
    details["Address"] = address
    details["Age"] = age
    details["Class"] = clas
    details["Roll no "] = roll

    if mod==99:
        temp = getdata.ReturnData()
        temp.append(details)
        return temp
    else:
        return details


def Writing_To_Disk(mod='w', filename="detail.json"):
    temp = Input_From_User()
    try:
        with open(filename, mod) as file:
            json.dump(temp, file)
            str=(f"\t\t  <--- Writing to Disk Sucessfully ----->")
            animation.ReadingFromString(str)

        file.close()
    except:
        str=(f"\t\t  <----- Unable to open File -----> ")
        animation.ReadingFromString(str)
    


# Writing_To_Disk()
# Input_From_User()
