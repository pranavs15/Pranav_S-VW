
def get_range():
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    return start, end



def print_odd():
    start, end = get_range()
    print("Odd numbers:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()



def print_even():
    start, end = get_range()
    print("Even numbers:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def print_all():
    start, end = get_range()
    print("All numbers:")
    for i in range(start, end + 1):
        print(i, end=" ")
    print()
