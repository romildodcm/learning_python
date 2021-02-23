# INHERITANCE - Demo

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
    def say_hello(self):
        # Let the parent do some work
        super().say_hello()
        # Add on custon code
        print('I am rather tired')
    # Returns the name on Student class
    def __str__(self) -> str:
        return f'{self.name} attends {self.school}'


# Using a derived class
student = Student('Romildo', "UMD")
print(student)
student.say_hello()
