import math

def estimate(terms=0, total_limit=0): # ax1 + ax2..... axN <= total_limit.
	try:
		x = total_limit/terms # Value of x or x <= val.

	except ZeroDivisionError:
		print("Cannot divide by zero")

	else:
		x_rounded = math.floor(x) # Rounds the value of 'x' to the greatest integer.

		# Prints the value of x, first without being rounded and then rounded.
		print(x, 'or', x_rounded, 'can satistfy the inequality', end='\n') 

		'''Substitutes the value of 'x' with the rounded integer and solves the 
		inequality'''
		print('After Substitution:', (terms * x_rounded), '<=', total_limit) 


# An example
estimate(10+15+30, 500)
