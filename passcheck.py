def pas():
    print("Welcome to password checker !")

    while True:
        password = input("Enter your password: ")
        length = len(password)

        if length >= 8 and length <= 32:
            print("your password is good in length")

            has_upper = False
            has_number = False

            for p in password:
                if p in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    has_upper = True
                if p in "1234567890":
                    has_number = True

            if has_upper:
                print("Your passord got capital leters too !")
                if has_number:
                    print(f"perfect congrates your password : {password} is perfect")
                    break
                else:
                    print("your password does not contain numbers, so it is high security but not recommended, please reenter the password")
                    continue
            else:
                print("There is no capital leter so, this password got intermediate security, please reenter password !")
                continue

        else:
            print("It doesn't meet criteria for length of password, it must be between 8 to 32 characters")
            continue

pas()
