a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice (1/2/3/4): "))
match choice:
    case 1: 
        result = a + b
        print("The result of addition is:", result)
    case 2:
        result = a - b
        print("The result of subtraction is:", result)
    case 3:
        result = a * b
        print("The result of multiplication is:", result)
    case 4:
        if b != 0:
            result = a / b
            print("The result of division is:", result)
        else:
            print("Error: Division by zero is not allowed.")