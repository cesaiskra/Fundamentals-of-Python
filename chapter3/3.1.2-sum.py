'''
Here is an example of a summation, which accumulates the
sum of a sequence of numbers from a lower bound through an upper bound:
'''

lower = input("enter the lower bound: ")
upper = input("enter the upper bound: ")

sum = 0 

for count in xrange(lower, upper + 1):
	sum = sum + count