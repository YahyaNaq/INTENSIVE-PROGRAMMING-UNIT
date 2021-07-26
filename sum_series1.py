# Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ... + 1/N

plus=0
n=int(input("Please enter the last term number of the required series: "))
for i in range(1,n+1):
    plus+=1/i
print("Sum of the given series is",plus)
