# 2) Write a program that accepts a list from user and print the alternate element of list.

user_list = input("Enter elements separated by space: ").split()

print("Alternate elements are:")
for i in range(0, len(user_list), 2):
    print(user_list[i])
