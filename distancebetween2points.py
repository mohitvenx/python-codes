#To find distance between 2 points
x=int(input('Enter values for x '))    #value of x co-ordinate
y=int(input('Enter values for y '))    #value of y co-ordinate
a=int(input('Enter values for a '))    #value of a co-ordinate
b=int(input('Enter values for b '))    #value of b co-ordinate
distance = ((((x-a)**2)+((y-b)**2))**0.5)  #formula to find distance between the 2 points
print(distance)