# Example 1: Simple overriding
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):  # override greet()
        print("Hello from Student")

p = Person()
p.greet()  # Hello from Person

s = Student()
s.greet()  # Hello from Student


# Example 2: Overriding with super()
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):
        super().greet()  # call parent method
        print("And hello from Student")  # add new behavior

s = Student()
s.greet()
# Output:
# Hello from Person
# And hello from Student


# Example 3: Overriding constructor (__init__)
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)  # call parent constructor
        self.year = year        # add new property

s = Student("Linus", 2026)
print(s.name, s.year)  # Linus 2026


# Example 4: Overriding a method to change behavior
class Shape:
    def area(self):
        return 0  # default

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):  # override area()
        return self.width * self.height

r = Rectangle(5, 3)
print(r.area())  # 15
