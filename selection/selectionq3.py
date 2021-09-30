print("please enter your order value")
a = int(input())
if a > 15:
    d = 0
else:
    d = 3.5
#endif
print("would you like free next day delivery, if so please enter 1")
b = int(input())
if b == 1:
    c = d + 5, print(c)
else:
    print(d)
#endif
