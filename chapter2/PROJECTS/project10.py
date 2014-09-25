'''
An employee's total weekly pay equals the hourly wage multiplied by the
total number of regular hours plus any overtime pay. Overtime pay equals
the total overtime hours multiplied by 1.5 times the hourly wage. Write a
program that takes as inputs the hourly wage, total regular hours, and
total overtime hours and displays an employee's total weekly pay.
'''

r = input("regular hours:")
o = input("overtime hours:")

w = input("hourly wage:")


p = r * w + o * w * 1.5

print = "weekly pay is $", p