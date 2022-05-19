from msvcrt import getch
import os
def DestoryingTheDatabase(filename="detail.json"):
    try:
        os.remove(filename)
        print(f"\t\t <---- Sucessfully Destory -----> ")
    except:
        print(f"\t\t <---- File not found ----> ")
    getch()