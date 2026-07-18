# BUILD BY MUHAMMAD TAHIR

while True:                # Apply loop
    try:
        title1 = "== SIMPLE CALCULATOR =="          # Center method
        print(title1.center(80))

        title2 = "== Operations =="                 # Center method
        print(title2.center(80))

        print("1 - Addition (+)")
        print("2 - Sbtraction (-)")
        print("3 - Multiply (*)")
        print("4 - Divide (/)")
        print("5 - Remainder (%)")
        print("6 - Floor division (//)")
        print("7 - Exponential/Power (**)")
        print("8 - Exit\n")

        title3 = "== Give numbers ==\n"                # Center method
        print(title3.center(80))

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        choice1 = int(input("Enter choice(1-5): "))           # if-else conditions

        if choice1 == 1:
            print(f"Addition result = {num1 + num2}\n")

        elif choice1 == 2:
            print(f"Subtraction result = {num1 - num2}\n")

        elif choice1 == 3:
            print(f"Multiplication result = {num1 * num2}\n")

        elif choice1 == 4:
            print(f"Division result = {num1 / num2}\n")

        elif choice1 == 5:
            print(f"Remainder result = {num1 % num2}\n")

        elif choice1 == 6:
            print(f"Floor division result = {num1 // num2}\n")

        elif choice1 == 7:
            print(f"Exponential/Power result = {num1 ** num2}\n")

        elif choice1 == 8:
            print("Thanks for using this program:)")
            break

        else:
            print("Invalid option")
            break

    except Exception as e:                    # Error handling
        print(f"Error occured: {e}.")