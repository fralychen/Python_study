#!/usr/bin/python
mintues = int(input("Enter mintues: "))
def Hours(b):
	n=b / 60
	m=b % 60
	print("%d H,%d M" %(n,m))
if mintues < 0:
	try:
		raise ValueError
	except ValueError:
		print("this is negative number.")
else:
	Hours(mintues)
