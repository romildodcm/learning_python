people = ['Ro', 'Ka', 'Li', 'Ma']
print('-----------------------------------')
print(f'Numero de nomes: {str(len(people))}')
index = 0
while index < len(people):
    print(people[index])
    index += 1
print('-----------------------------------')
print(people)
people.sort()
print(people)
print('-----------------------------------')

# outro jeito mais fácil de printar nomes em uma lista
#bem menor que os whiles acima
for name in people:
    print(name)
print('-----------------------------------')