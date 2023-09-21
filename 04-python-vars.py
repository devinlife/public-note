from icecream import ic

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._private_attribute = "This is private"  # this will be ignored in our conversion

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

# Usage:
obj = MyClass("John", 30)
print(obj.to_dict())  # {'name': 'John', 'age': 30}

print(vars(obj))
ic(obj)
ic()
ic(vars(obj))
ic()