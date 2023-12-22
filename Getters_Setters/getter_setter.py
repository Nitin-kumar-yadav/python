class Myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is show {self._value}")
    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value
        

obj = Myclass(10)
print(obj.ten_value)
obj.show()