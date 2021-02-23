# Cleanup with with comand

# Current working directory
cwd = './more_python_for_Beginners/demo_files/'

# Writing to a file
stream = open(cwd + 'output_16.txt', 'wt')
stream.write("Loren ipsum dolar")
stream.close() # This is REALLY IMPORTANT!

# USING TRY/FINALLY automatically close resources
# Re-writing with a try/finally
# If however, I try to open a file and something goes wrong, I still close it.
# This is really important to avoid errors the next time you run the code.  
try:
    stream = open(cwd + 'output_16.txt', 'wt')
    stream.write("Loren ipsum dolar")
finally:
    stream.close()

# SIMPLIFYING WITH *with* COMMAND
# Basically will take care os closing for me. This is the same as try/finally 
with open(cwd + 'output_16.txt', 'wt') as stream:
    stream.write('Loren ipsum dolar2')
# I can use this with command for any of these objects where there's that
# requirement to close it when you're done. Not only for file streams.