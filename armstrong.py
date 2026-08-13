a=str(input("Enter a number to check if it is an Armstrong number or not: "))
n=len(a)
sum=0
for i in range(0,n):
    sum+=int(a[i])**n
if int(a)==sum:
    print(a, "is an Armstrong number.")
else:
    print(a, "is not an Armstrong number.")