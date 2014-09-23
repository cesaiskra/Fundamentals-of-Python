'''
Write a program that takes the radius of a sphere (a floating-point num-
ber) as input and outputs the sphere's diameter, circumference, surface
area, and volume
'''

from math import pi

r = float(input("radius of a sphere is: "))

d = 2 * r  

c = 2 * pi * r

s = pi * r ** 2  

#Volume = 4 * Pi * R * R * R / 3
v = 4 * pi * r ** 3 *  / 3

print "diameter is", str(d)
print "circumference is", str(c)
print "surface area is" , str(s)
print "volume is" , str(v)
