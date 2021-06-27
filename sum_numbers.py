# Python Program to print sum of negative numbers, positive even numbers 
# and positive odd numbers in a list

lst=[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
sum_neg=0
sum_pos_even=0
sum_pos_odd=0
for i in range(len(lst)):
    num=lst[i]
    if num<0:
        sum_neg=sum_neg+num
    if num>0 and not(num%2):
        sum_pos_even=sum_pos_even+num
    if num>0 and num%2:
        sum_pos_odd=sum_pos_odd+num

print("Sum of negative numbers in the list are:",b)
print("Sum of positive even numbers in the list are:",c)
print("Sum of positive odd numbers in the list are:",d)
