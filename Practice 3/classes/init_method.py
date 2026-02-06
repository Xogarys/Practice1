# __init__() assigns values when object is created

class Person:
    def __init__(self, name, age):
        self.name = name  # set name property
        self.age = age    # set age property

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


# Without __init__(), we must set properties manually
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


# Another example with __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)


# Example with more properties
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city      # set city property
        self.country = country  # set country property

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
