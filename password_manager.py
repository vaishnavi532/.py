mast_pass=input("enter masrter password :")

def view():
    pass
    with open("password.txt",'r') as f:
        for line in f.readlines():
            d=(line.rstrip())
            print(d.split())
def add():
    name=input(" account name :")
    pwd=input(" password :")
    with open ('password.txt','a') as f:
        f.write(name + "|" + pwd)

    
while True:
    user_input=input("do you want to add or view the passwrd or  q to quit? ")
    if user_input=="q":
        break

    if user_input == "add":
        add()

    elif user_input =="view":
        view()
    else:
        print("invalid choice")
        continue