# Python Program to Compute the Value of Euler's Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!

n=int(input("Please input the number of terms: "))
e=1
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    e+=1/fact
print("Value of Euler's Number e: ", e)
