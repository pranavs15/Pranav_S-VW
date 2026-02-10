

import mod1

while True:
    print("\nChoice to Print numbers")
    print("1. Odd numbers")
    print("2. Even numbers")
    print("3. All numbers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mod1.print_odd()
    elif choice == 2:
        mod1.print_even()
    elif choice == 3:
        mod1.print_all()
    elif choice == 4:
        print("Exiting program. Bye 👋")
        break
    else:
        print("Invalid choice, try again!")
