# program to red information form json file
import json
from msvcrt import getch
import GetData as getdata
import animator as animation

def DisplayingToScreeenFromFile():
    """ This function is program to read data json file like 
    [{"Name": "Joker", "Address": "Maithawa", "Age": "22", "Class": "33", "Roll no ": "33"}]
    [{"Name": "Saroj", "Address": "Kohalpur", "Age": "33", "Class": "22", "Roll no ": "44"}]
    """

    str=(f"\n\t\t <--------- Welcome to Display section ---------> ")
    animation.ReadingFromString(str)
    num = 0
    temp = getdata.ReturnData(filename="detail.json")

    for var in temp:
        num+=1
        str=(f"\n\t\t\t   <------ Element no {num} -----> " )
        animation.ReadingFromString(str)

        str=(f"\n\t\t\t  <-------------------------------->\n")
        animation.ReadingFromString(str)

        for vale, kess in var.items():
            print(f"\t\t\t\t  {vale} ----> {kess} ")
                               
        print(f"\n",end='')


    str=(f"\n\t\t\t    Total Number of User ---> {num} ")
    animation.ReadingFromString(str)


# DisplayingToScreeenFromFile()
 