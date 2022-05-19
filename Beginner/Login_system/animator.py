from os import system
import time


def ReadingFromFile(filename,type=99): 
    """ This function is program to read one character which gives animation to program in CLI mode 
    and its read its raw information from file 
   
    """
    try:
        with open(filename,'r') as file:
            str=file.read()
        file.close()
    except:
        print("\t\t <----- File not founded -----> ")
    else:
        if type==99:
            ReadingFromString(str,0.01)
        else:
            ReadingFromString(str,0)

def ReadingFromString(str,speed=0.04):
    """ This function is program to read one character which gives animation to 
        program in CLI mode
        small text like greating speed ---> 0.05
        long text like art -----> 0.10
        By defualt speed is ----> 0.04 
        Speed can also be changed 
       
         """
    
    file=str
    for var in file:
        i=0
        length=len(var)
        while i<length:
            time.sleep(speed)
            print(var[i],end="")
            # print(var[i])
            i+=1
# ReadingFromFile("art/Art.txt") # These Three Lines is For Testing Purpose
# filde="\n\t\t\t <---- Welcome to program --->"
# ReadingFromString(filde,0.04)