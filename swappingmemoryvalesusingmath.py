x = 10
y = 18
print('BEFORE: ')
print('The memory of x is',id(x))
print('The memory of y is',id(y))
x = x + y
y = x - y
x = x - y
print('AFTER: ')
print('The memory of x is',id(x))
print('The memory of y is',id(y))