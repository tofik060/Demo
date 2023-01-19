#You are a pilot, cruising at an altitude of 33000 ft,
# you want to land your plane, to land your plane, you need
# to be under 5000ft take input from the pilot, what
# is your current altitude, and suggest
# the pilot to go around if the altitude is more than 10K feet,
# if its more than 5K suggest the pilot to land the plane
# by bringing it to 1000ft

p = int(input("Enter your 1st Height to the ground:- "))

if p == 33000:
    print("you want to land your plane")
    z = int(input("yes, So Enter 101 / No, So Enter 001:- "))

    if z == 101:
        print("to land your plane, you need to be under 10k ft")
        pil = int(input("Enter your 2nd Height to the ground:- "))

        if pil>=5000 and pil<=10000:
            print("its your current altitude:")
            y = int(input("yes, So Enter 102 / No, So Enter 002:- "))

            if y == 102:
                print("to land your plane, you need to be under 5000ft")
                pi = int(input("Enter your 2nd Height to the ground:- "))

                if pi == 5000:
                    print("its your current altitude:")

                print("You can land the plane on the runway")
                yes = int(input("yes, So Enter 103 / No, So Enter 003:- "))

                if yes == 103:

                    if pi >= 1000 and pi <= 5000:
                        print("Successfuly land")
                    else:
                        print("You can not land the plane on the runway")

                else:
                    print("if you are not land the plan, So you can go.")

            else:
                print("sorry, but you can't land the plane ")

    else:
        print("sorry, but you can't land the plane")

else:
    print("sorry, but you can't land the plane")


