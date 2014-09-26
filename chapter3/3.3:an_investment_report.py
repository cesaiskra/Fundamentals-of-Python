
"""
program: investment.py
author: ken

compute an investment report.

1. the input are
	starting investment amount
	number of years
	interest rate (an integer percent)

2. the report is displayed in talular form with a header.

3. computations and outputs:
	for each year
		compute the interest and add it to the investment
		print a formatted row of results for that year

4. the ending investment and interest earned are also displayed.
"""

#accept the inputs
startBalance = input("enter the investment amount:")
years =  input("enter the number of years:")
rate =  input("enter the rate as a %:")

#convert the rate to a decimal number
rate = rate / 100.0

#initialize the accumulator for the interest
totalInterest = 0.0

#display the header for the table
print "%4s%18s%10s%16s" % \
	  ("year", "starting balance", "interest", "ending balance")

#compute and display the results for each year
for year in xrange(1, years + 1):
	interest = startBalance * rate
	endBalance = startBalance + interest
	print "%4d%18.2f%10.2f%16.2f" % \
		  (year, startBalance, interest, endBalance)
	startBalance = endBalance
	totalInterest += interest

#display the totals for the period
print "ending balance: $%0.2f" % endBalance
print "total interest earned: $%0.2f" % totalInterest
