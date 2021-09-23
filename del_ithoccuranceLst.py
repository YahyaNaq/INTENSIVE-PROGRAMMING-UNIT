# Python Program to Remove the ith Occurrence of the Given Word in a List where Words can Repeat

lst=["ab","abc","ab","abcd"]
lst_new=[]
word=input("Which word do you want to remove: ")
a=int(input("Which occ of word you want to remove? Enter num: "))
iter=0
for i in lst:
    if i==word:
        iter+=1
        if a!=iter:
            lst_new.append(i)
    else:
        lst_new.append(i)
print(lst_new)
