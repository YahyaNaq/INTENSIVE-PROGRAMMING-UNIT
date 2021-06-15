# Python Program to read a number n & print the natural numbers summation pattern.

num=int(input("Enter a number: "))
sum1=0
pattern=""
for i in range(1,num+1):
	sum1+=i
	print(f"{pattern}{i}={sum1}")
	pattern+=str(i)+"+"
