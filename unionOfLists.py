# Python Program to Find the Union of two Lists

lst1=[1,3,5,6,7,9,10]
lst2=[1,2,3,4,6,8,10]
U_lst=lst2
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        U_lst.append(lst1[i])
print("Union of two lists:",U_lst)
