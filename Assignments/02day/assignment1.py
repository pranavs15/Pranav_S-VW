

# 1) Area and Perimeter of a Rectangle

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)
print("----------------------------------")


# 2) Celsius to Fahrenheit and vice-versa
choice = input("Type C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif choice.upper() == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid choice")
print("----------------------------------")


# 3) 4 Digit Number Operations
num = int(input("Enter a 4 digit number: "))

a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

print("Face values:", a, b, c, d)
print(f"{num} = {a*1000} + {b*100} + {c*10} + {d}")

reverse = d*1000 + c*100 + b*10 + a
print("Reverse number =", reverse)
print("----------------------------------")


# 4) Average of Three Numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

avg = (x + y + z) / 3
print("Average =", avg)
print("----------------------------------")


# 5) Maximum of Three Numbers (Function)
def maximum(a, b, c):
    return max(a, b, c)

p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
r = int(input("Enter third number: "))

print("Maximum number =", maximum(p, q, r))
print("----------------------------------")


# 6) Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
print("----------------------------------")


# 7) Positive, Negative or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
print("----------------------------------")


# 8) Telephone Bill Calculation

calls = int(input("Enter number of calls: "))
bill = 200

if calls > 100:
    calls -= 100
    if calls <= 50:
        bill += calls * 0.60
    else:
        bill += 50 * 0.60
        calls -= 50
        if calls <= 50:
            bill += calls * 0.50
        else:
            bill += 50 * 0.50
            calls -= 50
            bill += calls * 0.40

print("Total Telephone Bill = Rs.", bill)
print("----------------------------------")


# 9) Leap Year Check

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

print("----------------------------------")


# 10) Grade Based on Average Marks

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

average = (m1 + m2 + m3) / 3
print("Average =", average)

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
else:
    print("Grade F")
