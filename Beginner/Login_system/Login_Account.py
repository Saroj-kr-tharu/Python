import json
from msvcrt import getch
import animator as animation


def Login_Account():

    login_pass = False
    login_user = False
    str = "\n\t\t <------- Welcome To Login Account ----->"
    animation.ReadingFromString(str, 0.01)

    str = "\n\t\t\t   Enter Username ----> "
    animation.ReadingFromString(str, 0.01)
    user = input()

    str = "\t\t\t   Enter password ----> "
    animation.ReadingFromString(str, 0.01)
    passwod = input()
    try:
        with open("database/creaditial.json", 'r') as file:
            for var in file:
                dic = json.loads(var)
                # print(f"{dic}\n")
                for vale, kes in dic.items():
                    if vale == 'Username':
                        if user == kes:
                            login_user = True
                    if vale == 'Password':
                        if passwod == kes:
                            login_pass = True

        file.close()
    except:
        str="\t\t\t  <----- File not found  ----->"
        animation.ReadingFromString(str,0.01)
        return

    if login_user == True:
        if login_pass == True:
            str = "\t\t <----- Sucessfully Login  ----->"
            animation.ReadingFromString(str, 0.01)
            print(f"\n\t\t\t Username ---> {user} ")
            print(f"\t\t\t Password ---> {passwod} ")
        else:
            str = "\t\t\t <---- Incorrect password ---->"
            animation.ReadingFromString(str, 0.01)
    else:
        str = "\n\t\t\t <----- InCorrect Username ----> "
        animation.ReadingFromString(str, 0.01)


# Login_Account()  # Testing Purpose
