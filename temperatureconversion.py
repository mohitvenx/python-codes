celcius1 = int(input('Enter the temperature in celcius: '))             #enter the temperature in degree celcius
fahrenheit2 = int(input('Enter the temperature in fahrenheit: '))       #enter the temperature in degree fahrenheit
fahrenheit1 = (9*celcius1)/5 + 32
celcius2 = (fahrenheit2 - 32)*5/9
print('The temperature ', celcius1,'C in degree fahrenheit is ', fahrenheit1, ' F')
print('The temperature ', fahrenheit2,'F in degree fahrenheit is ', celcius2, ' C')