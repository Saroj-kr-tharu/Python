from msvcrt import getch
import animator as animation
import os
def DestoryingTheDatabase(filename="detail.json"):
    str=(f"\n\t\t <-------- Welcome To Destory Database Section -------> ")
    animation.ReadingFromString(str)
    try:
        str="\n\t\t\t Press y to confirm ---> "
        animation.ReadingFromString(str)
        ch=input()
        if ch=='y' or ch=='Y' :
             os.remove(filename)
             str=(f"\t\t\t    <---- Sucessfully Destory -----> ")
             animation.ReadingFromString(str)
        else:
            str=(f"\t\t\t    <---- Cancell -----> ")
            animation.ReadingFromString(str)
            return
    except:
        str=(f"\t\t\t    <---- File not found ----> ")
        animation.ReadingFromString(str)
    getch()
# DestoryingTheDatabase()