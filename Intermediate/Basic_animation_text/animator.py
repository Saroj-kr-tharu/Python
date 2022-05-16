import time


def red(filename):
    with open(filename,'r') as file:
        for var in file:
            i=0
            length=len(var)
            while i<length:
                time.sleep(0.5)
                print(var[i],end="")
                # print(var[i])
                i+=1
red("art/Art.txt")