#write a program to read alphabets except 'F','c','f','C'characters and print the characters 
alpha = input('enter any alphabet from a/A to z/Z: ')
while (alpha!='F' and alpha!='C' and alpha!='c' and alpha!='f'):
  print(alpha)  
  alpha = input('enter any alphabet from a/A to z/Z: ')
print("END")