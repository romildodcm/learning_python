# No property

# class Presenter():
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print("Hello " + self.name)

# presenter = Presenter('Ro')
# # presenter.name = "Romildo"
# presenter.say_hello()

# With property

class Presenter():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('In the getter')
        return self.__name

    @name.setter
    def name(self, value):
        print('In setter')
        # Validation here
        self.__name = value

presenter = Presenter("Romildo")
print(presenter.name)