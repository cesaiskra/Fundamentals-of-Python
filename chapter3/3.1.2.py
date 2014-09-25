'''
Loops that count through a range of numbers are also called count-
controlled loops. The value of the count on each pass is often used in computa-
tions. For example, consider the factorial of 4, which is 1 * 2 * 3 * 4 = 24. 
'''

product = 1

for count in xrange(4):
	product = product * ( count + 1 )
	
	
'''
for count in xrange(1,5):
	product = product * count
'''
	