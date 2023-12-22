class person:
    name = "Nitin"
    occupation = "Software Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
# a.name = "Shubham"
# a.occupation = "Software Engineer"
# print(a.name, a.occupation)
a.info()