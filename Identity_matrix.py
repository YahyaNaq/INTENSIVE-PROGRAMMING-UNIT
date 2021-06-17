# Python Program to Print an Identity Matrix

rows=int(input("Please enter number of rows: "))
for row in range(1,rows+1):
	for col in range(1,rows+1):
		if row==col:
			print(1,end=" ")
		else:
			print(0,end=" ")
	print()
