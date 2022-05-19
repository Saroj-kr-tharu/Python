import json
import animator as animation
main={}
def input_information():
    str="\n\t\t\t   Enter Username -----> "
    animation.ReadingFromString(str,0.01)
    username=input()
    main["Username"]=username

    str="\t\t\t   Enter Password ------> "
    animation.ReadingFromString(str,0.01)
    pasword=input()
    main["Password"]=pasword
    return main

def CreateAccount():

        str="\n\t\t <----- Welcome to Create Account Section ----> "
        animation.ReadingFromString(str,0.01)
        try:
            with open("database/creaditial.json",'a') as file:
                json.dump(input_information(),file)
                file.write("\n")
                str="\t\t   <------ Sucessfully Registered --------> "
                animation.ReadingFromString(str,0.01)
            file.close()
        except:
            str="\t\t <----- Error in Read and Write   ----->"
            animation.ReadingFromString(str,0.01)
            return
# CreateAccount() # For Testing Purpose