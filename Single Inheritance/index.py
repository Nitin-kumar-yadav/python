class animals:
    def __init__(self, name, species):
        self.species = species
        self.name = name

    def make_sound(self):
        print("Sound made by animal")

class Dog(animals):
    def __init__(self, name, breed):
        animals.__init__(self, name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Bark !")

class Cat(animals):
    def __init__(self, name, breed):
        animals.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Sound of cat!")

    def jump(self):
        print("Long jump!")

d = Dog("Dog", "Dog")
d.make_sound()

a = animals("Dog", "Dog")
a.make_sound()

c = Cat("Cat", "Cat")
c.make_sound()
c.jump()