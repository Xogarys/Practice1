# Inheritance example: Student inherits from Person
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # call parent constructor
        self.graduationyear = 2019      # add new property


# Another version without graduation year
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # just inherit parent properties


# Version with graduation year as parameter
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year      # set graduation year from argument

x = Student("Mike", "Olsen", 2019)


# Version with a method
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
        # method to greet student
