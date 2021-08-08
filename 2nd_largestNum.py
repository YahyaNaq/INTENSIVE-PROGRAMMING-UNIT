# Python Program to Find the Second Largest Number in a List

lst=[1,4,3,2,1,5]
a=lst[0]
lst1=[]
for j in lst:
    if j>a:
        lst1.append(j)
        a=j
print(lst1[-2])
