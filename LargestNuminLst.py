# Python Program to Find the Largest Number in a List

lst=[1,3,4,5,2,6,10,8,7,9]
a=lst[0]
for j in lst:
    if j>a:
        a=j
print(a,"is the largest number in the list!")
