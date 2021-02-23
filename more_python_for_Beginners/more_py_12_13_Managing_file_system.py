# MANAGING THE FILE SYSTEM
# All the common operations are built into Python
# Static os classless
# os.path
#  old style
# Class based
# Path from pathlib library
#  Python 3.6 or higher
#  Better performance as it can avoid calls to the OS  

# WORKING WITH PATHS
from pathlib import Path

# Where am I? What is the current working directory?
cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# Combine parts to create full path name by joining path and filename
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull Path:\n' + str(new_file))

# Does this exist? Check if  file exists
print('\nDoes that file exists? '+ str(new_file.exists()))

# Get the parent directory
parent = cwd.parent

# Is this a directory?
print('\nIs this a directory? ' + str(parent.is_dir()))

# Is this a file?
print('\nIs this a file? ' + str(parent.is_file()))

# List child directories
print('\n-----directory contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)

print('\n-----directory contents-----')
for child in cwd.iterdir():
    if child.is_dir():
        print(child)

cwd = Path('./more_python_for_Beginners/demo_files')

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))
# Get the file name
print('\nFile name: ' + str(demo_file.name))

# Get the extension
print('\nFile suffix: ' + str(demo_file.suffix))

# Get the folder
print('\nFile folder: ' + str(demo_file.parent.name))

# Get the size
print('\nFile size: ' + str(demo_file.stat().st_size))