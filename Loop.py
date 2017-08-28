secret_number = 7

while True:
    guess = int(input("Chosse a number between 1 ans 10 : "))

    if guess == secret_number:
        print("You got it")
        break