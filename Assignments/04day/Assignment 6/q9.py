# Question 9:
# Menu Driven String Program

def even_position(text):
    return text[1::2]

def odd_position(text):
    return text[0::2]

def string_length(text):
    return len(text)

def add_a(text):
    return text + ('a' * len(text))

text = input("Enter a string: ")

while True:
    print("\nA. Display characters from even position")
    print("B. Display characters from odd position")
    print("C. Display length of string")
    print("D. Add 'a' at the end length times")
    print("E. Exit")

    choice = input("Enter choice: ").upper()

    if choice == 'A':
        print("Even Position Characters:", even_position(text))
    elif choice == 'B':
        print("Odd Position Characters:", odd_position(text))
    elif choice == 'C':
        print("Length:", string_length(text))
    elif choice == 'D':
        print("Modified String:", add_a(text))
    elif choice == 'E':
        break
    else:
        print("Invalid choice!")
