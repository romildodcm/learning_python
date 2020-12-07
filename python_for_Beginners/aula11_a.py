first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
# Modo 1 de manipular e formatar strings
output = 'Hello, ' + first_name + ' ' + last_name
model_number = 1
final_out = 'Model: {0}:\n{1}\n-----------------------------'.format(model_number,output)
print(final_out)
# Modo 2 de manipular e formatar strings
output = 'Hello, {} {}'.format(first_name, last_name)
model_number += 1
final_out = 'Model: {0}:\n{1}\n-----------------------------'.format(model_number,output)
print(final_out)
# Modo 3 de manipular e formatar strings
# Esse tem uma apicação interessante, quando num documento vamos usar 
# a mesma variável em várias partes, ai colocamos op index dela 0, 1,..., n
output = 'Hello, {0} {1}'.format(first_name,last_name)
model_number += 1
final_out = 'Model: {0}:\n{1}\n-----------------------------'.format(model_number,output)
print(final_out)
# Modo 4 de manipular e formatar strings
# Only available in Python 3
# achei a mais prática e mais clara, autoexplicativa
output = f'Hello, {first_name} {last_name}'
model_number += 1
final_out = 'Model: {0}:\n{1}\n-----------------------------'.format(model_number,output)
print(final_out)