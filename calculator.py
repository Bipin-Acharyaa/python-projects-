print("Here is the simple Calculator !!\n")

def calc():
    print("Enter numbers for calc below !!")
    try:
        num1 = int(input("Enter a number:  "))
        num2 = int(input("Enter second number: "))

        print("What do you want to do?")
        print("1 = Addition")
        print("2 = Subtraction")
        print("3 = Multiplication")
        print("4 = Division")

        op = int(input("Type ops Here: "))

        if op == 1:
            print(f"The addition is {num1 + num2}")
        elif op == 2:
            print(f"The subtraction is {num1 - num2}")
        elif op == 3:
            print(f"The multiplication is {num1 * num2}")
        elif op == 4:
            print(f"The division is {num1 / num2}")
        else:
            print("Invalid operation chosen!")

    except ValueError:
        print("Please input valid numbers!")

calc()
