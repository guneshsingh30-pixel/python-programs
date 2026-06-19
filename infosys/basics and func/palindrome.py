def palindrome(n):
    temp=n
    rev=0
    while temp>0:
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    if rev==n:
        return True
    else:       return False

num=int(input("Enter a number: "))
if palindrome(num):
    print(num,"is a palindrome")        
else:    print(num,"is not a palindrome")