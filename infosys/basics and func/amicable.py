def check_amicable_numbers(num1, num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1+=i
    for i in range(1,num2):
        if num2%i==0:
            sum2+=i
    if sum1==num2 and sum2==num1:
        return True
    else:
        return False
    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))    
if check_amicable_numbers(num1, num2):
    print(num1,"and",num2,"are amicable numbers")   
else:
    print(num1,"and",num2,"are not amicable numbers")