# Python Program to Sort a List According to the Length of the Elements

lst=["a","pak","after","best","ab","eyvallah"]
for i in range(len(lst)):
    for j in range(len(lst)):
        if len(lst[i])<len(lst[j]):
            lst[i],lst[j]=lst[j],lst[i]
print("Sorted list:",lst)
