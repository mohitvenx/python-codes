#Grades depending on marks
marks = int(input('Enter the marks obtained '))
if (marks>=90):
  print('You recieved A+ grade')
elif (marks>=80):
  print('you recieved A grade')
elif (marks>=60):
  print('You recieved B grade')
elif (marks>=50):
  print('You recieved C grade')
elif (marks>=40):
  print('You recieved D grade')
else:
  print('You failed in the subject')