"""
Classes define data structures and behavior

Why use classes
- Creat reusable components
- Group data and operations together

Moving parts
- Classes are nouns
- Properties are adjectives
- Methods are verbs

"""

# Creating a class
# In Pyton by convention uses PascalCasing for classes names,
# capital letter
# class Presenter():
#     def __init__(self, name):
#         # Constructor
#         self.name = name
#     def say_hello(self):
#         #method
#         print('Hello, ' + self.name)

# # Using a class 
# presenter = Presenter('Chris')
# presenter.name = 'Christopher'
# Presenter.say_hello()

# EVERYTHING IS PUBLIC
# Conventions for suggesting accessibility
# _ means avoid unless you really know what you're doing
#       ->  When I create a class and I put in a field or a method with
#           a single underscore, is I'm saying "yeah, I know that some
#           people are going to use that, I want to avoid changing it."
#           But there is no garanteed to the user that it's not going
#           to change at a late time and what I'm trying to tel the user
#           is "hey you probably don't want this, unless you really know
#           what's going on the internals of the class that I have created".
# __ (double underscore) means *do not use*
#       ->  "hey, don't use this!"
# If I see this in an library, follow that convention. And you're willing
# to accept the risk that whatever in there might change, that it might
# break your code.

# To control better the accessibility
# Setting up a property/ adding properties
class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name

    # Set up name as property (allows x = presentes.name and x receives
    # the name)
    @property
    def name(self):
        return self.__name
    # Allows presentes.name = 'Romildo' and gives opportunity to run some 
    # validation
    @name.setter
    def name(self, value):
        # cool validation here
        self.__name = value
    
    def say_hello(self):
        #method
        print('Hello, ' + self.name)

# Using a property

presenter = Presenter('Ro')
presenter.name = 'Romildo'
# Here I can print the name returned by the property
print(presenter.name)

presenter.say_hello()