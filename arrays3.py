outlet1sales = [10,12,15,10]
outlet2sales = [5,8,3,6]
outlet3sales = [10,12,15,10]
count = 0
for count in range(0,4):
    totalsales = outlet1sales[count] + outlet2sales[count] + outlet3sales[count]
    print("total for quarter",count+1,totalsales)
