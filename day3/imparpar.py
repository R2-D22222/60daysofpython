enter = input("Type the number:\n")

try:
    number = int(enter)
    if number % 2 == 0:
        print("par number")
    else:
        print("impar number")
except ValueError:
    print("You did not type int number")