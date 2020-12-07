'''
Write a function called right_justify that receives a string called s as a parameter and print the string with spaces in the front that make the last character of the string will be in column 70 of the screen.
'''

def right_justify(s):
    length = len(s)
    output = (70-length)*" "
    output = output+s
    print(output)

input_text = str(input())
right_justify(input_text)