#string encoding
s='We love python coding very much'
for i in s.split():               #for the first letter of each word is printed at the end.
 print(i[1:],end=" ")
 print(i[0],end=" ")

print('\n')

print('p'.join(s))       #for In the second case, after each character, a p is printed.