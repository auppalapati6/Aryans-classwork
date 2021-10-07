
import random
computer_choice = ['rock','paper','scissors']
a = (random.choice(computer_choice))
print("enter  your choice, a:rock, b:paper, c:scissors")
d = str(input())
print("the computer chose", a)
if a == "rock" and  d == "a":
    print("it is a tie")
elif a == "paper" and d == "b":
    print("it is a tie")
elif a == "scissors" and d == "c":
    print("it is a tie")
elif a == "rock" and d == "b":
    print("you lose")
elif a == "rock" and d == "c":
    print("you win")
elif a == "paper" and d == "a":
    print("you win")
elif a == "paper" and d == "c":
    print("you lose")
elif a == "scissors" and d == "a":
    print("you lose")
elif a == "scissors" and d == "b":
    print("you win")
else:
    print("invalid choice")
