a=int(input("Enter number of terms:"))
b=0
c=1
next=""
for i in range(0, a):
    if b<=a:
        print(b,end=",")
        next=b+c
        b=c
        c=next 