# Question 1:
# Define a function intersection() that takes two lists and returns
# another list that has common elements in both lists.

def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


# Example
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("Intersection:", intersection(list1, list2))
