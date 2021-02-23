# Demo - Working with files

# Current working directory
cwd = './more_python_for_Beginners/demo_files/'

# READ
stream = open(cwd + 'demo2.txt', 'rt')
print('\nIs this readable? ' + str(stream.readable()))
print('\nRead one character: ' + stream.read(1))
print('\nRead to end of line: ' + stream.readline())
print('\nRead all lines to end of file:\n' + str(stream.readlines()))

# WRITE
stream = open(cwd + 'output_15.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()))

stream.write('H') # Write a single character/string
stream.writelines(['ello', ' ', 'world']) # Write one or more strings
stream.write('\n') # Write a new line
names = ['Name 0', 'Name 1']
stream.writelines(names)
stream.write('\n')
# Here's a neat trick to insert a new line between items in the list
names = ['Name 2', 'Name 3']
stream.writelines('\n'.join(names))

# MANAGE
# Open manage.txt file to write text
stream = open(cwd + 'manage.txt', 'wt')
# Write the word demo to the file stream
stream.write("demo!")
# move back to the start of the file stream
stream.seek(0)
# Write the word cool to the file stream
stream.write("cool")
# Flush the stream contents to the file buffer
stream.flush()
# Flush the file stream and flose the file
stream.close()


