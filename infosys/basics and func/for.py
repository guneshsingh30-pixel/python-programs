
# # for number in range(1,5):
#      print ("The current number is ",number)
# print("---------------------------")
# for number in range(1,7,2):
#      print ("The current number is ",number)
# print("---------------------------")
# for number in range(5,0,-1):
#      print ("The current number is ",number)
num=int(input("enter a number:"))
sum=0
for i in range(0,len((str(num)))):
    sum=sum+int(str(num)[i])
print("The sum of first",num,"numbers is",sum)