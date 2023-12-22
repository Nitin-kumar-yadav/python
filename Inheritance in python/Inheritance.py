class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the id of the employee is {self.id}")


class Programmer(Employee):
    def showLanguages(self):
        print("The default language is python")

e = Employee("Nitin",12)
e2 = Programmer()
e.showDetails()
e2.showLanguages()
e2.showDetails()