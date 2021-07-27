# Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n

Sum=1
nth=int(input("Please enter the last term number of the required series:"))
x=int(input("Please enter x of the given series: "))
for i in range(2,nth+1):
    Sum+=x**i/i
print("Sum of the given series is:",Sum)
