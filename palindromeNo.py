a=str(input("enter number to check if number is palindrome or not: "))
n=len(a)
rev=""
for i in range(n):
    rev+=a[n-i-1]
if a==rev:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")