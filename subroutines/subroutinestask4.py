
#display menu of options
car_park =[]
for row in range(20):
  car_park.append([])
  for col in range(6):
    car_park[row].append('empty')
  #next col
#next row
print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
option = input("Enter your choice: ")
while option != "5":
    
    if option == "1":
        car_park.clear
        print("empty car park")
        print("would you require further actions")
        a = input()
        if a == "yes":
            temp = 9
        else:
            option =  option +str(100)
    elif option == "2":
        registration = input("please enter your registration")
        row = input("what row is the car in")
        column = input("what column is it in")
        car_park[int(row)][int(column)] = registration
        print(car_park)
        print("would you require further actions")
        a = input()
        temp = 3
        if a == "yes":
            temp = 9
        else: 
            option = option + str(100)
    elif option == "3":
        car_park.remove(registration)
        print(car_park)
        print("would you require further actions")
        a = input()
        temp = 3
        if a == "yes":
            temp = 9
        else: 
            option = option + str(100)
    elif option == "4":
        print(car_park)
        print("would you require further actions")
        a = input()
        temp = 3
        if a == "yes":
            temp = 9
        else: 
            option = option + str(100)
    elif option == 101 or option == 102 or option == 103 or option == 104:
        print("task done")
    else:
        option = ("Invalid choice - please re-enter: ")
    
    #endif
print("1. Reset all spaces in the car park to ‘empty’")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit\n")
#endwhile
print("Goodbye") 
