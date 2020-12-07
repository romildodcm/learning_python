# Sometimes we receive a input data with a date as a string
# and we need to convert it to a datetime object
# follow this example

from datetime import datetime, timedelta

birthday = input('When is your birthday (dd/mm/yyyy)? ')
# convert to date object
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: '+ str(birthday_eve))


