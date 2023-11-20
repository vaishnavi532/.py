import random
rand_range=int(input("enter a number\n"))
if rand_range<0:
    print("please enter a number more than zero")
    quit()
n=random.randint(0,rand_range)
guess_count=0
while True:
    guess_count+=1
    guess=int(input("enter your guess :"))
    if guess==n:
        print("your right!")
        break
    else:
        print("your wrong")

    if guess >n:
        print("your above my guess*_*")
    else:
        print("your below my guess ^_^")

print("you guessed number in",guess_count,"rounds")
