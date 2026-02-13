# Question 7:
# Convert list and tuple of integers into list of strings using map.

list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)

list_strings = list(map(str, list_numbers))
tuple_strings = list(map(str, tuple_numbers))

print("List converted to strings:", list_strings)
print("Tuple converted to strings:", tuple_strings)
