from datetime import datetime, timedelta

today = datetime.now()
print('Today is: '+str(today))

# timedelta is used to define period of time
one_day = timedelta(days=1)
yesterday = today - one_day

print('Yesterday was: ' + str(yesterday))


# If I need to use only a current day, month or year? Ok, so..

current_date = datetime.now()

print('Day: '+str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: '+str(current_date.year))
