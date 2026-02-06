# Example 1: Simple class variable
class Dog:
    species = "Canine"  # class variable shared by all dogs

    def __init__(self, name):
        self.name = name  # instance variable unique for each dog

dog1 = Dog("Buddy")
dog2 = Dog("Lucy")

print(dog1.name)    # Buddy (instance variable)
print(dog2.name)    # Lucy
print(dog1.species) # Canine (class variable)
print(dog2.species) # Canine


# Example 2: Counting number of objects using a class variable
class Person:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Person.count += 1  # increase class variable

p1 = Person("Emil")
p2 = Person("Tobias")
p3 = Person("Linus")

print(Person.count)  # 3 (total number of Person objects)


# Example 3: Using class variable for default value
class Car:
    wheels = 4  # default number of wheels

    def __init__(self, model):
        self.model = model

c1 = Car("Toyota")
c2 = Car("Honda")

print(c1.model, c1.wheels)  # Toyota 4
print(c2.model, c2.wheels)  # Honda 4


# Example 4: Changing class variable for all objects
class Student:
    school = "ABC High School"  # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Linus")
s2 = Student("Emil")

print(s1.school)  # ABC High School
print(s2.school)  # ABC High School

# change class variable
Student.school = "XYZ Academy"

print(s1.school)  # XYZ Academy
print(s2.school)  # XYZ Academy
