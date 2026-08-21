a=int(input("Enter number of terms:"))
b=0
c=1
print("Fabonacci sequence:")
for i in range(a):
    print(b, end=",")
    b, c=c, b+c