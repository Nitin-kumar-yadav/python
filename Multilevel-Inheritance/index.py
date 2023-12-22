class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
    
class Dog(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animals.show_details(self)
        print(f"Breed : {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color : {self.color}")

o = GoldenRetriever("Tommy", "black")
o.show_details()
print(GoldenRetriever.mro())