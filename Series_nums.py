# Python Program to read a number n & print the series "1+2+…..+n= "

n=int(input("Please input a number: "))
series=""
sum=0
for i in range(1, n+1):
	sum+=i
	if i!=n:
		series+=str(i)+"+"
	else:
		series+=str(i)+"="+str(sum)
print(series)

