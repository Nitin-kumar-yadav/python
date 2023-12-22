# class Shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x*self.y
    
# class Circle(Shape):
#     def __int__(self,radius):
#         super().__init__(radius, radius)
#         def area(self):
#             return 3.14 * super().area()


# # rec = Shape(3,5)
# # print(rec.area())

# c = Circle(5,5)
# print(c.area())

#!/bin/python3


n = int(input("Number"))
for i in range(n):
    n = n + 1
    n = n*n
    print(n)

