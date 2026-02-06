# Example 1: Simple multiple inheritance
class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def skills(self):
        print("Gardening")

class Child(Mother, Father):  # inherits from both Mother and Father
    pass

c = Child()
c.skills()  # Cooking (Mother comes first in order)


# Example 2: Using methods from both parents
class Mother:
    def cooking(self):
        print("Can cook")

class Father:
    def gardening(self):
        print("Can garden")

class Child(Mother, Father):
    pass

c = Child()
c.cooking()   # Can cook
c.gardening() # Can garden


# Example 3: Overriding a method in multiple inheritance
class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def skills(self):
        print("Gardening")

class Child(Mother, Father):
    def skills(self):
        print("Programming")  # override parent methods

c = Child()
c.skills()  # Programming


# Example 4: Constructor in multiple inheritance
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Child(Mother, Father):
    def __init__(self, mother_name, father_name, child_name):
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name = child_name

c = Child("Anna", "John", "Mike")
print(c.mother_name, c.father_name, c.child_name)  # Anna John Mike
