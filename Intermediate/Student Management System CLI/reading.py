# program to red information form json file
import json
from msvcrt import getch
def DisplayingToScreeenFromFile(filename="detail.json"):
    """ This function is program to read data json file like 
    [{"Name": "Joker", "Address": "Maithawa", "Age": "22", "Class": "33", "Roll no ": "33"}]
    [{"Name": "Saroj", "Address": "Kohalpur", "Age": "33", "Class": "22", "Roll no ": "44"}]
    """
   
    print(f"     <--------- Welcome to Display section ---------> ")
    num=0
    try:
        with open("detail.json",'r') as file:
            for var in file:
                dic=json.loads(var)
                num+=1
                print(f"\t\t <-----  Element {num} ----->")
                for vale,kes in dic.items():
                    print(f"\t\t   {vale} -----> {kes} ")
                print(f"\n")
        print(f"\t\t  Total No User ---> {num}")
        file.close()
    except:
        print(f"\t\t <----- File Not Founded ---->")

DisplayingToScreeenFromFile()