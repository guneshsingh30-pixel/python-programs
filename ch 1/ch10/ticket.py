from random import randint
class Train:
    def __init__(self,traino):
        self.traino=traino
    def book(self,fro,to):
        print(f"Ticket is booked in tarin no:{self.traino} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no: {self.traino} is running on time")
    def getfare(self,fro,to):
        print(f"Ticket no:{self.traino} from {fro } to {to} is {randint(444,999)}")

t=Train(12399)
t.book("kanpur","Delhi")
t.getstatus()
t.getfare("Kanpur","delhi")