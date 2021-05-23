n=int(input("Enter number of terms "))
def fib(n):
 if n==0 or n==1:
   return n
 else:
   return(fib(n-1)+fib(n-2))

for i in range(n):
 print(fib(i))



'''
x=[10,20]
def f(a,b=x):
 b.append(a)
 return b
x=[11,22]
print(f(30))
print(f(5,[1,2]))
print(f(50))
'''