class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(DerivedClass, Derived2):
    pass