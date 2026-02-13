# Question 4:
# Create lambda functions that convert:
# tons → kilograms → grams → milligrams → pounds.
# Input weight in tons and print remaining units.

# 1 ton = 1000 kg
# 1 kg = 1000 g
# 1 g = 1000 mg
# 1 mg = 0.00000220462 pounds

conversions = [
    lambda t: t * 1000,           # tons to kg
    lambda kg: kg * 1000,         # kg to g
    lambda g: g * 1000,           # g to mg
    lambda mg: mg * 0.00000220462 # mg to pounds
]

tons = float(input("Enter weight in tons: "))

kg = conversions[0](tons)
g = conversions[1](kg)
mg = conversions[2](g)
lbs = conversions[3](mg)

print(f"{kg} kg")
print(f"{g} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
