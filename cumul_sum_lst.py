# Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List

lst1=[1,2,3,4,5]
lst2=[]
for i in range(len(lst1)):
    ind=0
    for j in range(i+1):
        ind+=lst1[j]
    lst2.append(ind)
print("Origin list: {}\nCumulative sum list: {}".format(lst1,lst2))
