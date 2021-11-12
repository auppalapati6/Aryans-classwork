alphabet = [0]*5
print("input your 5 letters")
for i in range(0,4):
    alphabet[i] = str(input())

max = -10000000
min = 10000000
for i in range(0,4):
    if alphabet[i] > max:
        max = alphabet[i]
    if alphabet[i] < min:
        min = alphabet[i] 
print(alphabet)

