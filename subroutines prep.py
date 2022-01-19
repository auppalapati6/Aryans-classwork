names = []
def displaymenu():
    x = 0
    while x == 0:
        print("press 1 to add a name, press 2 to display the list, press 3 to exit")
        userinput = input()
        if input == 1:
            print("what name do you want to add")
            inputname = input()
            names.append(inputname)
        elif input == 2:
            print(names)
        elif input == 3:
            print("you have quit")
            x = 1
        else:
            print("invalid choice")

