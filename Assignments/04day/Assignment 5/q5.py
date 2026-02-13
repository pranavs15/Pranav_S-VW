# Extension:
# CAPTCHA Functionality
# Generate a random string and ask user to retype it correctly.

import random
import string

print("CAPTCHA Verification System")

captcha_length = 6
characters = string.ascii_letters + string.digits

captcha = ''.join(random.choice(characters) for _ in range(captcha_length))

print("\nCAPTCHA:", captcha)

user_input = input("Please retype the CAPTCHA exactly: ")

if user_input == captcha:
    print("✅ Verification successful!")
else:
    print("❌ Incorrect CAPTCHA. Please try again.")
