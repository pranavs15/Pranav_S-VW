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