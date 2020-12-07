# The datetime library for work with time, to manipulate dates
from datetime import datetime

#this function returns a datetime object 
current_time = datetime.now()
# If we need to print this, just convert the data/object into a string
# just like we convert numbers into a string
print('Today is: '+str(current_time))