# Python Program to Find the LCM of Two Numbers
# (This program is only valid for non-zero numbers)

num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))
div=2
lcm=1
while num1>1 or num2>1:
    while not(num1%div) or not(num2%div):
        lcm*=div
        if num1%div==0:
            num1/=div
        if num2%div==0:
            num2/=div
    div+=1
print("LCM:",lcm)
