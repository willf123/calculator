while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
    else:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        if choice == "1":
            result = first_number + second_number
            print("Answer:", result)

        elif choice == "2":
            result = first_number - second_number
            print("Answer:", result)

        elif choice == "3":
            result = first_number * second_number
            print("Answer:", result)

        elif choice == "4":
            if second_number == 0:
                print("Error: Cannot divide by zero")
            else:
                result = first_number / second_number
                print("Answer:", result)

        again = input("Calculate again? (yes/no):")
        if again == "no":
            break