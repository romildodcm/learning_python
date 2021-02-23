"""
PEP 8 - All about formatting

Common rules:
 - Spaces, not tabs
 - variable_name, not variableName or VariableName (uses the first)
 - Avoid extraneous whitespace: {'good': 42} { 'bad' :20 }

Uses Linting in your environment, It's common for all languages, 
Pylint for Python, how to install:

# Windows
pip install pylint

# Linux or macOS
pip3 install pylint

Linting is configurable to ignore certain rules, but avoid doing this.
"""
from time import sleep
from colorama import init, Fore
from random import randint

"""
The first 'str' says this variable is going to be a string and the
second 'str' says that the function will go to return a string.
The docstring inside the function will be presented by the IntelliSense
when putting the mouse cursor over the function.
"""
def get_color_greeting(name: str) -> str:
    """
    Returns a greeting in a randon color

    Parameters:
        name (str): The name of the person

    Returns:
        The cool message
    """
    color = ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']

    terminal_color = getattr(Fore, color[randint(0, 6)])
    print(terminal_color + 'Hello, ' + name)

# When puts the mouse cursor over the function name,
# does not present the type of input or output
def greeting(name):
    return 'Hello, ' + name

"""
With this specification, the parameter needs to be an str type
and when puts the mouse cursor over the function name, will be
present the type of input and maybe present the output type
"""
def get_greeting(name: str):
    return 'Hello, ' + name

message = get_greeting('Julhinha')
print(message)

while True:
    # Put the mouse cursor over the function name and test
    get_color_greeting('Julhinha')
    sleep(60)