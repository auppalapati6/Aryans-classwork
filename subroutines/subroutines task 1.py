def test1():
    print("hello")
#end procedurea

test1()

print("what is your name")    
Name = input() 
print("enter table, starting number and ending number")
Table = input()
Startnum = input()
Endnum = input()

def multiples() : 
   print("hi",Name)
   for x in range(Startnum,Endnum+1):
       print("your talble is,", Table, "start number is", Startnum, "ending number is", Endnum, x*Table)
multiples()



