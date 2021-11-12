pasword = "tues1212"

counter = 0
while counter<3:
    attempt=input()
    if attempt == pasword:
       print("password accepted")
    elif attempt !=pasword:
        print("password rejected")
        counter = counter+1
