# Python Program to Merge Two Lists and Sort it

lst1=[4,2,1,5,3]
lst2=[8,6,0,10,12]
merged=lst1+lst2
for i in range(len(merged)):
    for j in range(len(merged)):
        if merged[i]<merged[j]:
            merged[i],merged[j]=merged[j],merged[i]
print(f"Merged list: {merged}")
