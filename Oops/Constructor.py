class person:
    # name = "Nitin"
    # occ = "Developer"
    def __init__(self, name, occ):
        print("Hey I am a constructor")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Nitin", "Developer")
b = person("Shubham", "HR")
a.info()
b.info()
# print(a.name,a.occ)
# print(a.info())
