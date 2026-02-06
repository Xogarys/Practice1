# Example 1: Simple class with a method
class Person:
    def __init__(self, name):
        self.name = name  # store the name

    def greet(self):
        print("Hello, my name is " + self.name)  # method to greet

p1 = Person("Emil")
p1.greet()


# Example 2: Calculator class with basic methods
class Calculator:
    def add(self, a, b):
        return a + b  # add two numbers

    def multiply(self, a, b):
        return a * b  # multiply two numbers

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


# Example 3: Class with a birthday method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # store name and age

    def celebrate_birthday(self):
        self.age += 1  # increase age by 1
        print(f"Happy birthday! You are now {self.age}")  # print message

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


# Example 4: Class without __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1)  # prints object info, not readable


# Example 5: Class with __str__ for readable print
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"  # customize print

p1 = Person("Tobias", 36)
print(p1)  # now prints: Tobias (36)
