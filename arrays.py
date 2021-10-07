numbers = []
counter = 0 
while counter < 6:
    x = int(input("type in a number"))
    numbers.append(x)
    counter = counter + 1
#endwhile

print (numbers)


counter = 5
while counter >= 0:
    print(numbers[counter])
    counter = counter - 1
#endwhile