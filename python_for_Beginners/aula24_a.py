# A student makes honour roll if their average ir >= 85
# and their lowest grade is not below 70

gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Conditions
#if gpa >= .85 and lowest_grade >= .70:
#    print('You made the honour roll!')

# Conditions with bolean
if gpa >= .85 and lowest_grade >= 0.7:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made the honour roll')