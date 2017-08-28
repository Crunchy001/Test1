while True:
    try:
        number = int(input("Please enter a number : "))
        break
    except ValueError:
        print("It's not a number")
    except:
        prin("Inconnu")
print("merci")