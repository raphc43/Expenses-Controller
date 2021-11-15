import math

def estimate(terms=0, total_limit=0): # aq1 + aq2..... aqN <= total_limit.
	try:
		q = total_limit/terms # Value of q or x <= val.

	except ZeroDivisionError:
		print("Cannot divide by zero")

	else:
		q_rounded = math.floor(q) # Rounds the value of 'q' to the greatest integer.

		# Prints the value of x, first without being rounded and then rounded.
		print(q, 'or', q_rounded, 'can satistfy the inequality', end='\n') 

		'''Substitutes the value of 'x' with the rounded integer and solves the 
		inequality'''
		print('After Substitution:', (terms * q_rounded), '<=', total_limit) 


# An example
estimate(10+15+30, 500)
