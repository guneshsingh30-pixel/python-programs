class vectors:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return vectors(self.x + other.x,self.y + other.y,self.z + other.z)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __str__(self):
        return f"vector({self.x} , {self.y} , {self.z})"
    def __len__(self):
        return 3
v1=vectors(1,2,3)
v2=vectors(4,5,6)
v3=vectors(8,9,7)
print(v1+v2)
print(v1*v2)
print(v3+v2)
print(v3*v2)
print(len(v1))