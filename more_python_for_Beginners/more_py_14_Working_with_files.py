# WORKING WITH FILES
# Opening a file
# stream = open(file_name, mode, buffer_size)
#
# Modes:
# -> r - Read (default)
# -> w - Truncate and write
# -> a - Append if file exists
# -> + - Updating (read/write)
# 
# -> t - Text (default)
# -> b - Binary 

# Current working directory
cwd = './more_python_for_Beginners/demo_files/'

# Reading from a file
stream = open(cwd + 'demo.txt')

print(stream.readable()) # Can we read?
print(stream.read(1)) # Read the first character
print(stream.readline()) # Read a line
stream.close() # Close the stream

# Writing to a file
stream = open(cwd + 'output.txt', 'wt') # Write text
stream.write('H') # Write a single string
stream.writelines(['ello',' ','world']) # Write multiple strings
stream.write('\n') # Write a new line
names = ['Romildo', 'Yuki'] # Create a list of things
stream.writelines(names) # Write list of things
stream.close() # close the stream (and flush data)

# Managing the stream
stream = open(cwd + 'output2.txt', 'wt')
stream.write('demo!')
stream.seek(0) # Put the cursor back at the start
stream.write('cool2')
stream.flush() # Write the data to file
stream.close() # Flush and close the stream