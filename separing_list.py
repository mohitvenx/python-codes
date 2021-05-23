l=['pani puri','dosa','bhel puri','masala dosa','dahi puri','rava dosa','pizza topings','pizza mania']
pizza=[]
puri=[]
dosa=[]
for i in l:
 if i.startswith('pizza'):
  pizza.append(i)
 elif i.endswith('puri'):
  puri.append(i)
 else:
  dosa.append(i)
print(pizza,dosa,puri)