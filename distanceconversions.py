km = int(input('Enter distance in kms: '))                                 #Enter the distance between the 2 places in kilometers
m = km*1000                                                                #converting kilometers to meters
cm = m*100                                                                 #converting kilometers to centimeters
ft = km*3280.84                                                            #converting kilometers to feet
inch = km*39370.08                                                         #converting kilometers to inches
print('The given distance ', km,'km in meters is equal to ', m)            #result for distance in meters
print('The given distance ', km,'km in centimeters is equal to ', cm)      #result for distance in centimeters
print('The given distance ', km,'km in feet is equal to ', ft)             #result for distance in feet 
print('The given distance ', km,'km in inches is equal to ', inch)         #result for distance in inches