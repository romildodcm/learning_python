# INHERITANCE
# Creates an "is a" relationship
# -> Student is a Person
# -> SqlConnection is a DatabaseConnection
# -> MySqlConnection is a DatabaseConnection
# 
# COMPOSITION (with properties) creates a "has a" relationship
# -> Student has a Class
# -> databaseConnection has a ConnectionString
#
# Python inheritance in action
# All methods are "virtual"
# -> Can override or redefine their behavior
# Keyword *super* to access parent class
# -> Constructor
# -> Properties in methods
# Must always call parent constructor


# Inheritance from a class
class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, ' + self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)

# Using a derived class
student = Student('Romildo', "UMD")
student.say_hello()
student.sing_school_song()

# What are you?
# Is this in instance of additional classes?
print(f'Is this a student? {isinstance(student, Student)}') # return true becouse student is Student
# student is a person return true 
print(f'Is this a person? {isinstance(student, Person)}') # return true becouse student is a Person
# is a Student a subclass of Person? In another words, does it inherit?
# return true becouse of the fact that we inherit
print(f'Is Student a Person? {issubclass(Student, Person)}') 

