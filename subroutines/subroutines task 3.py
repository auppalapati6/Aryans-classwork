
# msg = ('h','e','l','l','o')
# msg2 = 'hello'


# print(msg, len(msg))
# print(msg2, len(msg2))

# print(msg[2])
# print(msg2[2])


def getpword():
    attempt = 1
    password1 = 1
    password2 = 1
    passwordinput1 = str(input("please enter your passwod"))
    temp = len(passwordinput1)
    #print(attempt)
    #print(passwordinput1)
    #print(len(passwordinput1))
    #print(temp)
    if attempt == 1 and 8 > len(passwordinput1) > 3:
        password1 == passwordinput1
        attemp = attempt+1
        passwordinput2 = input("please reenter your password")
        if passwordinput2 == passwordinput1 and attempt == 2:
            print("password change accepted")
            password2 = passwordinput2
        else:
            print("password does not match")
    else:
        print("password invalid")
getpword()