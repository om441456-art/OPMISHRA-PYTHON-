tm=True
while tm:
   a=str(input("Enter a name to reverse: "))
   print("You have enterd: ",a)
   n=len(a)
   rev=""
   for i in range(0,n):
       rev+=a[n-i-1]
   print("Reversed name is:",rev)

   again = input("\nDo you want to continue? (y/n): ")
   if again == "Y" or again == "y":
      tm=True
   else:
      tm=False
      print("\nThank you for using my softwere. Goodbye!")
    