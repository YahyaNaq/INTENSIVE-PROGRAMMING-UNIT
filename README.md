# Avg-of-nums
This code calculates the average of numbers in a user entered list

add=0
num=[]
n=int(input("How many numbers do you want average of: "))
for i in range(n):
    nums=eval(input("Enter number: "))
    num.append(nums)
    add+=num[i]
avg=add/n
print("The average of your given numbers is",avg)
