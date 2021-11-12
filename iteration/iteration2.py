pasword = "tues1212"

counter = 0
while counter<3:
    attempt=input()
    if attempt=password:
       print("password accepted")
    elif attempt !=password:
        print("password rejected")
        counter = counter+1
endwhile