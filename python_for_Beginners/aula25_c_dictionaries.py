# Dictionaries 
# Lists: zero based index and storage order guaranteed
# Dictionaries: Key/Value pairs and storage order not guaranteed

romildo = {}
romildo['first'] = 'Hu'
romildo['last'] = 'Bei'


user = {}
user['first'] = 'Lia'
user['last'] = 'Cheng'

people = []
people.append(romildo)
people.append(user)
people.append({
    'first': 'Li', 'last': 'Chang'
})

print(people)