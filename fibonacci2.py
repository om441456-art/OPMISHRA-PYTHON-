n=int(input("Enter the number of terms: "))
first=0
second=1
for i in range(n):
    if first <= n:
        print(first, end=" ")
    
    first, second = second, first + second