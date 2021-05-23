#TO FIND THE FIRST EVEN ELEMENT IN THE GIVEN LIST 
found=False
l=[99,97,87,85,20,90, 80, 35, 9, 5, 4, 3, 2]
i=0
while not found and (i<len(l)):
 if l[i]%2==0:
  found=True
 else:
  i+=1
if found:
 print('found',l[i] )
else:
 print('not found')