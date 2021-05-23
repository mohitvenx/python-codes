#Finding the gravitational force between two objects
G=6.673*(10**-11)
m1 = float(input('Enter mass of first object: ')) 
m2 = float(input('Enter mass of first object: '))
r = float(input('Enter the distance between m1 and m2: '))
F = (G*m1*m2)/(r**2)
print('The gravitational force between the 2 objects is', F, 'N')