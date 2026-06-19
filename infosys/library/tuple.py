n=int(input("enter the no of passengers:"))
ticket_no=101
tickets=[]
for i in range(n):
    src=input("enter the source CITY:")
    dest=input("enter the destination CITY:")
    ticket="AL1"+src[:3].upper()+dest[:3].upper()+str(ticket_no)
    tickets.append(ticket)
    ticket_no+=1
if n<5:
    print(tickets)
else:
    print(tickets[-5:])