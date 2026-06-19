n=int(input("Enter number:"))
first=0
second=1
if(n==0):
    print(first)
elif(n==1):
    print(first)
    print(second)
    print(second)
else:
    print(first)
    print(second)
    for i in range(3,n+1):
        sum=first+second
        print(sum)
        first=second
        second=sum