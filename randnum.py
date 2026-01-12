import random

def game():
    randnum = random.randint(1, 100)
    print("Lets guess number , lets see in how many tries you gonna find it !!")
    x = 0

    while True:
        try:
            num = int(input("Enter a number between 1 and 100: "))

            if not (1 <= num <= 100):
                print("Please input again in between 1 and 100")
                continue

            x += 1

            if num > randnum:
                print("You are high")
            elif num < randnum:
                print("You are low")
            else:
                print(f"You got it in {x} tries!")
                break

        except ValueError:
            print("Enter a number not variable !")

game()
