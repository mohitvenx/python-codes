#Given 'mohanDas Karamchand gandhi'  print  i)"m K gandhi" ii) M K GANDHI  iii) M K Gandhi   iv) Mohandas Karamchand Gandhi

s= 'mohanDas Karamchand gandhi' 
ss=" "
namelist=s.split()
for i in namelist[:len(namelist)-1]:
 ss=ss+i[0]+" "

ss=ss+namelist[-1]
print(ss)
print(ss.upper())
print(ss.title())
print(s.title())