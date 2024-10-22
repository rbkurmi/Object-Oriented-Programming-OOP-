class Person:
    def __init__(self, name, age):
        self.name = name         # Public attribute
        self._age = age          # Protected attribute
        self.__ssn = "123-45-6789"  # Private attribute

person = Person("John", 30)

print(person.name)  # Public: accessible
print(person._age)  # Protected: accessible, but by convention should not be
# print(person.__ssn)  # Private: will raise AttributeError
