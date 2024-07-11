import random

a = random.randint(1, 100)

while True:
    answer = int(input("Enter a number between 1 and 100: "))
    if answer == a:
        print("You win!")
        break
    elif answer < a:
        print("more")

    elif answer > a:
        print("smaller")
    else:
        print("Invalid number")
