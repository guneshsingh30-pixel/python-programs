def check_strong_number(num):
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        f=1
        for i in range(1,dig+1):
            f=f*i   

        sum+=f
        temp=temp//10
    if sum==num:
        return True 
    else:        return False
num=int(input("Enter a number: "))
if check_strong_number(num):    
    print(num,"is a strong number")        
else:    print(num,"is not a strong number")