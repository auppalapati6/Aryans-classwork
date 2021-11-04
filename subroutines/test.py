
def multiples(table, startnum, endnum, pupilname):
    for x in range(startnum,endnum+1):
      print(("hello",pupilname, x, "X", table, "is ", x*table))
#end procedure
pupilname = input("what is your name")
print("enter table, starting number and ending number")
table = int(input())
startnum = int(input())
endnum = int(input())
    
multiples(table,startnum,endnum,pupilname)