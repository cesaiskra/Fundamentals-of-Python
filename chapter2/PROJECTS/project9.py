'''
Write a program that takes as input a number of kilometers and prints the
corresponding number of nautical miles. Use the following approximations:

- A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
- There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
- A nautical mile is 1 minute of an arc.

'''

n = 10000.0
km = n / 10000.0
nm = n / 90.0 / 60.0
rate = km / nm

i = input("input kilometers: ")
print i, "kliometers = ", rate * i  , " nautical miles" 
