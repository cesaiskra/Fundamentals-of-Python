'''
Five Star Video rents new videos for $3.00 a night, and oldies for $2.00
night. Write a program that the clerks at Five Star Video can use to calculate
the total charge for a customer's video rentals. The program should prompt
the user for the number of each type of video and output the total cost.
'''

new = input("how many new videos:")
old = input("how many old videos:")


print "total cost is: $",  str(3.0 * int(new) + 2.0 * int(old))
