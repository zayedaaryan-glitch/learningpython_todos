

while True:

    password = input("please enter a strong password")

    strong = {}

    if len(password) <= 8:
        strong["length"] = False
    else:
        strong["length"] = True

    num = False
    for char in password:
        if char.isdigit():
            num = True

    strong["digits"] = num

    caps = False
    for char in password:
        if char.isupper():
            caps = True

    strong["capitalization"] = caps

    if all(strong.values()):
        print("Password is strong.")
        break
    else :
        print("Password is not strong. Try again")


