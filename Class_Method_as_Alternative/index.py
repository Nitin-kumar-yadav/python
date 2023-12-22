class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromString(cls, string):
        return cls(string.split(' ')[0], string.split(' ')[1])

e = Employee("Nitin",56565)
print(e.name, e.salary)

string = "Nitin 165661"
e1 = Employee(string.split(" ")[0], int(string.split(" ")[1]))
print(e1.name, e1.salary)

string = "Amit 200"
e2 = Employee.fromString(string)
print(e2.name)
print(e2.salary)