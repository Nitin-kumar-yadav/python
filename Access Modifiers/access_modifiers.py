class Employee:
    def __init__(self):
        self.__name = "Nitin"

a = Employee()
# print(a.__name)  Cannot be accessed directly
print(a._Employee__name) #Can be accessed Indirectly
# print(a.__dir__())