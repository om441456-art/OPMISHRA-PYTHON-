a=str(input("Enter a name to check if it is palindrome or not: "))
print("You have enterd: ",a)
n=len(a)
rev=""
for i in range(0,n):
    rev+=a[n-i-1]
if rev==a:
    print("Its a palindrome name")
else:
    print("Its not a palindrome name")