class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_info = {
    "name": "John",
    "age": 30,
    "iiage": 30
}
person = Person(**person_info)
print(person.name)  # 출력: John
print(person.age)   # 출력: 30
