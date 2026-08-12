a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print("before swapping: a=", a, "b=", b)
a=a+b
b=a-b
a=a-b
print("after swapping: a=", a, "b=", b)