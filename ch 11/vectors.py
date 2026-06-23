class twovectors:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vectors is {self.i}i + {self.j}j")
class threevectors(twovectors):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k     
    def show(self):
        print(f"the vectors is {self.i}i + {self.j}j + {self.k}k")

a=twovectors(1,2)
b=threevectors(1,2,3)
a.show()
b.show()