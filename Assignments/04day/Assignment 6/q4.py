# Question 4:
# Translate text into rövarspråket (robber's language).

def translate(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + "o" + char
        else:
            result += char

    return result

text = input("Enter text: ")
print("Translated:", translate(text))
