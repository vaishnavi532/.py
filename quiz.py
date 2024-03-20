print("Let's play Quiz...!")
a=input("Are you ready to play:) ")

c=0
if a.lower()!= "yes":
    quit()
print("Your questions will be here :")
b=input("what is CPU ?")
if b.lower()=="central processing unit":
    c+=1
    print("your Right!")
else :
    print("WRONG!")

d=input("what is API ?")
if d.lower()=="application program interface":
    c+=1
    print("your Right!")
else :
    print("WRONG!")
print(c, " total correct")
