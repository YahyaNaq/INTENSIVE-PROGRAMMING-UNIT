# Python Program to Find the Intersection of Two Lists

lst1=[1,3,5,6,7,9,10]
lst2=[1,2,3,4,6,8,10]
I_lst=list()
for i in range(len(lst1)):
    if lst1[i] in lst2:
        I_lst.append(lst1[i])
print("Intersection of two lists:",I_lst)
