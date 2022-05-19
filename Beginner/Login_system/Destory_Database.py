import os
import animator as animation

def DestoryDataBase():
    try:
        str="\n\t\t <----- Welcome to Destory Database Section ----> "
        animation.ReadingFromString(str,0.01)
        os.remove("database/creaditial.json")
    except:
        str="\n\t\t\t <---- File is not Founded ----> "
        animation.ReadingFromString(str,0.01)
        return
    else:
        str="\n\t\t\t <----- Sucessfully Delete Database -----> "
        animation.ReadingFromString(str,0.01)
# DestoryDataBase()