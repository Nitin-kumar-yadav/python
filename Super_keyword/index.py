# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Nitin")
#         # super().parent_method()
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()

# child_object = ChildClass()
# child_object.parent_method()
# child_object.child_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id,)
        self.language = language

obj = Employee("Nitin",10)
object = Programmer("Ashvani", 20, "Python")
# print(obj.name,obj.id)
# print(object.name, object.id, object.language)
print(object.name, object.id, object.language)