a = int(input("\nEnter first number: "))
b = int(input("\nEnter second number: "))
print("\nINSTRUCTIONS: Choose an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("\nEnter your choice (1-4): "))
if operation == 1:
    result = a + b
    print("\nThe addition of", a, "and", b, "is", result)
elif operation == 2:
    result = a - b
    print("\nThe subtraction of", a, "and", b, "is", result)
elif operation == 3:
    result = a * b
    print("\nThe multiplication of", a, "and", b, "is", result)
elif operation == 4:
    if b != 0:
        result = a / b
        print("\nThe division of", a, "and", b, "is", result)
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid operation choice. Please select a number between 1 and 4.")