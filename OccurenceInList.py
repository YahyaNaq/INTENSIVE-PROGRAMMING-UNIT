# Python Program to Search the Number of Times a Particular Number Occurs in a List

lst=[1,2,3,4,1,5,2,4,6,7,3,1,4,5]
num=int(input("Please enter the number you want to check: "))
count=0
for i in lst:
    if i==num:
        count+=1
print("Number of times {} occurs in list is: {}".format(num,count))
