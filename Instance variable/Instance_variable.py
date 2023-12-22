class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.05

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the amount is {self.raise_amount}")

emp1 = Employee("Nitin")
emp1.raise_amount = 0.1
emp1.showDetails()

emp2 = Employee("Shivam")
emp2.showDetails()