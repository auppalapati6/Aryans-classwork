def evennums(n):
    if n<=0:
        return 0
    if not n % 2 == 0:
        return evennums(n-1)
    else:
        return n + evennums(n-2)
      
print(evennums(10))
