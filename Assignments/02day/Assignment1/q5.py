# 5) Maximum of Three Numbers (Function)
def maximum(a, b, c):
    return max(a, b, c)

p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
r = int(input("Enter third number: "))

print("Maximum number =", maximum(p, q, r))