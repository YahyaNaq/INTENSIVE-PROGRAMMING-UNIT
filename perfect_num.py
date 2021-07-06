# Python Program to Check if a Number is a Perfect Number

p_num=int(input("Please enter a number for checking: "))
p_sum=0
for i in range(1,p_num//2+1):
    if not(p_num%i):
        p_sum+=i
if p_num==p_sum:
    print("Yes your given number is a perfect number!")
else:
    print("Sorry!")
