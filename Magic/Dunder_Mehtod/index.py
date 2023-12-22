class Employee:
    name = "Nitin"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

e = Employee()
print(e.name)
print(len(e))