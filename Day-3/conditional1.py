print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print(" You can ride the Roller Coaster")
    age = int(input("What is your age?"))
    if age<=18:
        print("You get a ticket of $7")
    elif age>18:
        print("You get a ticket of $12")
else:
    print("You can't ride the Roller Coaster")