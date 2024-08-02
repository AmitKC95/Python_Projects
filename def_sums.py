def sum_of_numbers(x):
    total = 0
    for i in range(1, x+1):
        total += i
    return total

print(sum_of_numbers(5))


def sum_numbers():
    n = int(input("Enter a number - "))
    totals = 0
    for m in range(1, n+1):
        totals += m
    print(totals)

sum_numbers()