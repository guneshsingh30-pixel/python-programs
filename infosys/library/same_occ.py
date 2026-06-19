l=int(input("Enter the length of the list: "))
list1=[]
count=0
i=0
print("Enter the elements of the list: ")   
for i in range(l):
    element=input()
    list1.append(element)
for i in range(0,len(list1)-1):
    if (list1[i]==list1[i+1]):
        count+=1
print(count)