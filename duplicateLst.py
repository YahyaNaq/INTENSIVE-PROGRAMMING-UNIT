# Python Program to Remove the Duplicate Items from a List

lst=[1,2,3,2,5,4,3,2,1,8]
i1=0
i2=1
while i1<len(lst):
    e1=lst[i1]
    while i2<len(lst):
        e2=lst[i2]
        if e1==e2 and i1!=i2:
            lst.remove(e2)
        i2+=1
    i1+=1
    i2=0
print("List without duplicate elements is:" ,lst)
