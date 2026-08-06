a = int(input("\nEnter number to get sum of all numbers from 1 to that number: "))
sum = 0
for i in range(1, a + 1):
    sum += i
print("Sum of all numbers from 1 to", a, "is: ", sum)