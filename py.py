#!/usr/bin/python
row = int(input("Enter the number of rows: "))
while row >= 0:
	x = "*" * row
	y = " " * (row - 1)
	print(x+y)
	row -= 1
