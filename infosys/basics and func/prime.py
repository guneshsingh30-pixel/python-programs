num=int(input("enter number"))
count=0
for i in range(2,10):
    if(num%i==0):
        count+=1
    
if(count<=1):
    print("Prime")
else:
    print("not a prime")