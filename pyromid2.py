a = int(input("Enter a number to get the inverted pyramid: "))
for i in range(a, 0, -1):
    print(" " * (2 * (a - i)) + "*   " * i)