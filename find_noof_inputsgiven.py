#print the positive numbers provided by user and total no.of numbers entered
num = int(input('Enter the number'))
cout=0
sum=0
while num>0:
  sum = sum + num
  num = int(input('Enter the number'))
  print('The number entered is ',num)
  cout = cout + 1
  if(num =='0'):
    break
print('No.of inputs are',cout )
print('Sum of inputs is ', sum)
  