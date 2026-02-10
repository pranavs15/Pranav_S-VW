# 8) Telephone Bill Calculation

calls = int(input("Enter number of calls: "))
bill = 200

if calls > 100:
    calls -= 100
    if calls <= 50:
        bill += calls * 0.60
    else:
        bill += 50 * 0.60
        calls -= 50
        if calls <= 50:
            bill += calls * 0.50
        else:
            bill += 50 * 0.50
            calls -= 50
            bill += calls * 0.40

print("Total Telephone Bill = Rs.", bill)