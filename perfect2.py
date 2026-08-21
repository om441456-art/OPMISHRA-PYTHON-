a=int(input("Enter limit to check how many perfect numbers are there: "))
sum=0
for i in range(1,a+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(sum,"is a perfect number")
    