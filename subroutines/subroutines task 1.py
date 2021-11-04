def test1():
    print("hellow")
#end procedurea

test1()

def multiples(table, startnum, endnum, name):
    name = input("what is your name")
    print("hello", name)
    print("enter table, starting number and ending number")
    table = int(input())
    startnum = int(input())
    endnum = int(input())
    for x in range(startnum,endnum+1):
      print((x*table))

multiples()