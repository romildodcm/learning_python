# Arrays are also collections of items
# Arrays: store numerical data types must all be the same type
# Collections: store anything, store eny type
from array import array

#'d' is for the double type, for int use 'i' and for float use 'f'
scores = array('d')
scores.append(97)
scores.append(98)

print(scores)
print(scores[1])