
a=int(input('Enter first value '))
b=int(input('Enter second value '))
print('a and b value before swap is ', a,',', b)
a=a^b     
b=a^b          
a=a^b
print('a and b value after swap is ', a,',', b)