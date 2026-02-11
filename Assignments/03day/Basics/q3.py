# 3) WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.

marks = {}

for i in range(3):
    subject = input("Enter subject name: ")
    score = int(input("Enter marks: "))
    marks[subject] = score

print("Final dictionary:", marks)
