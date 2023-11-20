import random
option=["rock","paper","scissor"]
user_count=0
computer_count=0
while True:
    user_choice=input("Type either rock ,paper or scissor or Q to quit :").lower()

    if user_choice=="q":
        quit()
    if user_choice not in option:
         continue

    random_choice=random.randint(0,2)
    computer_pick=option[random_choice]
    print( "computers choice is",computer_pick)

    if user_choice=="rock" and computer_pick=="scissor":
         user_count+=1
         print("you won!")

    elif user_choice=="paper" and computer_pick=="rock":
         user_count+=1
         print("you won!")
    elif user_choice=="scissor" and computer_pick=="paper":
          user_count+=1
          print("you won!")
    else:
        computer_count+=1
        print("computer won!")
        break

print("user won",user_count,'times')
print("computer won",computer_count,'times')
print("bye bye!!!")