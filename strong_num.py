# Python Program to Check if a Number is a Strong Number

num=int(input("Please enter a three digit number: "))
fact1=1
fact2=1
fact3=1
dig1=num//100
dig2=(num%100)//10
dig3=(num%100)%10
for i in range(dig1//dig1,dig1+1):
    fact1=fact1*i
for j in range(dig2//dig2,dig2+1):
    fact2=fact2*j
for k in range(dig3//dig3,dig3+1):
    fact3=fact3*k
if fact1+fact2+fact3==num:
    print("Yes, your entered number is a strong number!")
else:
    print("Sorry, your entered number is NOT a strong number!")
