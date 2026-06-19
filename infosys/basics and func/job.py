salary=float(input("Enter the current salary:"))
level=float(input("enter the job level:"))
new=0
if(level==3):
    new=((15/100)*salary)+salary
    print("the new salary is:",new)
elif(level==4):
    new=((7/100)*salary)+salary
    print("the new salary is:",new)
elif(level==5):
    new=((5/100)*salary)+salary
    print("the new salary is:",new)
else:
    print("the salary will be",salary)