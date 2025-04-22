
def strength(password):
    if len(password) >= 8:
        print("strong password")
    elif len(password) < 8:
        print("normal password")
    elif len(password) < 4:
        print("too short password") 
    else:
        print("enter valid password")

password = input("enter your password: ")

strength(password)

