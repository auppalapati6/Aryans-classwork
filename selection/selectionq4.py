print("enter your attendance")
a = int(input())
print("enter your examn score")
b = int(input())
if a < 90:
    print("you have failed")
elif b > 90:
    print("you have got an A")
elif 90 > b > 80:
    print("you have gotten a B")
elif 80 > b > 70:
    print("you have gotten a C")
elif b < 70:
    print("you have failed")
else:
    print("you have failed") 
