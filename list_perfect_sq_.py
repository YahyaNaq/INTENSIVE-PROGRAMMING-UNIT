# Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

from math import *
Range=input("How many numbers do you want to check? ")
lst=[]
for num in range(10,int(Range)+11):
    if num>9:
        sum_dig=num//10+num%10
    if num>99:
        sum_dig=num//100+(num%100)//10+num%100%10
    if num>999:
        sum_dig=num//1000+(num%1000)//100+num%1000%100//10+num%1000%100%10
    if not(sqrt(num)%1) and sum_dig<10:
        lst.append(num)
print(lst)
