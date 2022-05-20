# Program to return data 

import json

def ReturnData(filename="detail.json"):
    with open(filename,'r') as file:
        data=file.read()
        final=json.loads(data)
    file.close()
    return final
    # print(f"\t\t Final ---> {final}")

# print(f"\t\t Reutrn data ---> {ReturnData()} ")
# ReturnData()
