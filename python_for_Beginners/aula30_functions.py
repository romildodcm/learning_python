from datetime import datetime
#Function to print date and time
def task_completed(task_name):
    print(task_name)
    print(datetime.now())
    print()

f_name = 'Romildo'



task_completed('Print the first name')

for x in range(0,10):
    print(x)

task_completed('Completed loop for')