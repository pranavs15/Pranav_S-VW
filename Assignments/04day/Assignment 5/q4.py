# Question 4:
# Random Password Generator (Console App)
# Generates secure password with:
# - Uppercase letters
# - Lowercase letters
# - Digits
# - Special characters

import random
import string

print("Random Password Generator")

length = int(input("Enter password length (8–12 recommended): "))

# Ensure minimum security requirements
if length < 4:
    print("Password length should be at least 4.")
else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"

    remaining_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))

    password_list = list(uppercase + lowercase + digit + special + remaining_chars)
    random.shuffle(password_list)

    password = ''.join(password_list)

    print("\nGenerated Password:", password)
