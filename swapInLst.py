# Python Program to Swap the First and Last Value of a List

lst=[1,2,3,4,5]
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print(lst)

lst1=[1,2,3,4]
lst1[0],lst1[-1]=lst1[-1],lst1[0]
print(lst1)
