# Error handling demo
# ok, go for launch! 
#How to use try-except finally 

x = 42
y = 0

print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()