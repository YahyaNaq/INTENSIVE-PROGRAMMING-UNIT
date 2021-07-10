# Python Program to Find the GCD of Two Numbers

num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))
if num1>=num2:
    gcd=num2
else:
    gcd=num1
while 1:
    if not(num1%gcd) and not(num2%gcd):
        print("GCD:",gcd)
        break
    else:
        gcd-=1
