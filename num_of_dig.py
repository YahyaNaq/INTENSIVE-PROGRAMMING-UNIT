# Python Program to count the number of digits in a number

num=int(input("Please input a number: "))
n=0
while num>0:
    num//=10
    n=n+1
print("There are {} digits in the given number".format(n))
