# Python Program to Find the Second Largest Number in a List Using Bubble Sort

lst=[1,3,2,5,6,9,4,8,7,10]
for i in range(len(lst)):
    for n in range(len(lst)):
        if lst[i]<lst[n]:
            lst[i],lst[n]=lst[n],lst[i]
print("Second largest number:",lst[-2])
