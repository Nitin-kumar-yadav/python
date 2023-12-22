# def cube(x):
#     return x*x

# print(cube(2))

# l = [1,2,3,4,5,6,7,8,9,10]
# newl = list(map(cube,l))
# print(newl)

# def filter_function(a):
#     return a>4
# newl1 = list(filter(filter_function, l))
# print(newl1)

from functools import reduce
number = [1,2,3,4,5,6,7,8,9,10]

def mysum(x, y):
    return x+y

sum = reduce(mysum, number)
print(sum)