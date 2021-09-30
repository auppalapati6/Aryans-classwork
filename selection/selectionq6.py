print("please choose what type of car you would like, enter either economy, saloon or sports")
a = str(input())
if a != "sports" and a != "economy" and a != "saloon":
    print("invalid selection")
elif a == "sports":
    print("you have chosen a sports car")
elif a == "economy":
    print("you have chosen an economy car")
elif a == "saloon":
    print("you have chosen a saloon car")
else:
    print("you have not chosen")