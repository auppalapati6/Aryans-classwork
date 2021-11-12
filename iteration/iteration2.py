pasword = "tues1212"
"enter your password"

counter = 0
while counter<3:
    attempt=str(input())
    if attempt == pasword:
       print("password accepted")
    elif attempt !=pasword:
        print("password rejected")
        counter = counter+1
#endwhile