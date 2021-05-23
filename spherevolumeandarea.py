#To find volume and surface area of a sphere
radius = int(input('Enter the radius of the sphere '))
pi = 3.14
volume = (4*pi*(radius**3))/3
sa = 4*pi*(radius**2)
print('The volume of sphere whose radius is', radius,'cm is', volume,'cm^3')
print('The surface area of sphere whose radius is', radius,'cm is', sa,'cm^2')