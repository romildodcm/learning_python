#Collections
# Collections: store anything, store eny type

names = ['Ro', 'Wa', 'Bruno', 'Maisa', 'Sabrina', 'Ana', 'Denilson', 'Chen']

scores = []
scores.append(98) # add new item to the end
scores.append(99)

print(names[0])
print(names[4])


print(scores)

print(scores[0]) # Collections are zero-indexed
print(scores[1])
print('-----------------------------------')

# Comum operations 
print(names)
print(len(names)) #get the number of items
names.insert(0, 'Bill') # Insert before index
print(len(names))
print(names)
names.sort() #Alphabetic ordem
print(names)
print('-----------------------------------')

# Retrieving ranges
presenters = names[1:5] # 1 e 3 are start and end index
# De 0 até um index pode ser sem adicionar o zero
a = names[:3]

print(names)
print(presenters)
print(a)

