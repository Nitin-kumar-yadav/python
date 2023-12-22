class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


v = Vector(3,4,5)
print(v)
v2 = Vector(1,6,8)
print(v2)
print(v+v2)
print(type(v+v2))