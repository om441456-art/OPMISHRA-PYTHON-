a=int(input("Enter a number to check if it is a perfect number or not: "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")