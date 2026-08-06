a=int(input("Enter number of even numbers to count: "))
ct=0
for i in range(a):
    if i % 2 == 0:
        ct += 1
print("Total even numbers:", ct)