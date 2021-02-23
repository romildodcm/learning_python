"""
If I want to sort this list of dictionaries I'll have problem

presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort()
print(presenters)


Follow the example of how to resolve this:
"""

#I can:

def sorter(item):
    return item['name']

presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

print('With normal function: ')
presenters.sort(key=sorter)
print(presenters)

"""

Works fine, but see that small function, for this I can use something
called a Lambda function:
"""
print('With Lambda function (sort by alphabetical): ')
# This lambda function will be used to sort by alphabetical order
presenters.sort(key=lambda item: item['name'])
print(presenters)

# This another lambda function will be used to sort by str length order
print('With Lambda function (sort by string length): ')
presenters.sort(key=lambda item: len(item['name']))
print(presenters)