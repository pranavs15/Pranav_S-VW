# Question 8:
# Menu Driven Program to Calculate Perimeter and Area of
# Circle, Square, Rectangle using functions.

import math

def circle():
    r = float(input("Enter radius: "))
    print("Area:", math.pi * r * r)
    print("Perimeter:", 2 * math.pi * r)

def square():
    s = float(input("Enter side: "))
    print("Area:", s * s)
    print("Perimeter:", 4 * s)

def rectangle():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", l * w)
    print("Perimeter:", 2 * (l + w))

while True:
    print("\n1. Circle\n2. Square\n3. Rectangle\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        circle()
    elif choice == '2':
        square()
    elif choice == '3':
        rectangle()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
