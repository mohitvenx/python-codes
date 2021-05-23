#To find the distance between given latitudes and longitudes
from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending latitude: ")))
elat = radians(float(input("Starting longitude: ")))
elon = radians(float(input("Ending longitude: ")))
#Finding the distance b/w them 
dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is ",dist,'km')