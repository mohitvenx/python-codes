'''found=False
l=[90, 80, 35, 9, 5, 4, 3, 2]
i=0
while not found and (i<len(l)):
 if l[i]%2==0:
  found=True
 else:
  i+=1
if found:
 print('found',l[i] )
else:
 print('not found')'''



"""def outer():
 x = 10 #local
 print('within outer x:',x)
 def inner():
  nonlocal x
  x = 20 #x from outer funtion
  print('within inner x:',x)
 inner()
x = 5 #global
print('Before outerx:',x)
outer()
print('After outer x:',x)"""


"""def func(a=[], b={}):
 print(a)
 print(b)
 print('*' * 6)
 a.append(len(a))
 b[len(a)]=len(a)
func()
func()
func()
func(a=[1, 2, 3], b={'B': 1})
func()"""


def len(*s):
 max = 0
 for strgs in s:
  if len(strgs) > max:
   max = len(strgs)
   return max
x=len('narendraModi','RahulGandhi','AmitShah','Yogi')
print(x)
