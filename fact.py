a = int(input("Enter number to get factorial: "))
fact = 1
for i in range(1, a + 1):
    fact *= i
print("Factorial of", a, "is:", fact)