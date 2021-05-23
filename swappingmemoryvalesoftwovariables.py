x = 10
y = 18
print('BEFORE: ')
print('The memory of x is',id(x))
print('The memory of y is',id(y))
c = x
y = c
x = 18
print('AFTER: ')
print('The memory of x is',id(x))
print('The memory of y is',id(y))