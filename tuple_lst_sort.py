# Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

lst=[(1,3),(1,2,4),(5,1),(6,3,5,2),(1,2,3)]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i][-1]<lst[j][-1]:
            lst[i],lst[j]=lst[j],lst[i]
print("List sorted according to the last element in tuples:",lst)
