class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

d = DancerEmployee('Kathak', 'Shivani')
print(d.name)
print(d.dance)
d.show()