# x = [1,2,3,4,5]
# print(dir(x))

class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Persion("Nitin", 300)
print(p.__dict__)
print(help(Persion))