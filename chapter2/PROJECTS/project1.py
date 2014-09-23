"""
The tax calculator program of the case study outputs a floating-point
number that might show more than two digits of precision. Use the
round function to modify the program to display at most two digits of
precision in the output number.
"""

# Initialize the constants

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossIncome = input("Enter the gross income:")
numDependents = input("Enter the number of dependents:")

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
				DEPENDENT_DEDUCTION * numDependents

incomeTax = round(taxableIncome * TAX_RATE, 2) #   round(number[, ndigits]) -> floating point number

# Display the income tax
print "The income tax is $" + str(incomeTax)
