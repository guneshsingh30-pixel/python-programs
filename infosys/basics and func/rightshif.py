def rightshift(num,n):
    result=num>>n
    print(num,"right shifted by",n,"is",result)
    return result
num=int(input("Enter a number: "))
n=int(input("Enter number of bits to right shift: "))   
rightshift(num,n)
