# Python Program to Detect if Two Strings are Anagrams

str1=input("Please input first string: ")
str2=input("Please input second string: ")
count1=0
count2=0
for i in range(len(str1)):
    a=str1[i]
    for j in str1:
        if a==j:
            count1+=1
    for k in str2:
        if a==k:
            count2+=1
    if count1!=count2:
        break
if i==len(str1)-1:
    print("The two strings are anagrams!")
else:
    print("The two strings are NOT anagrams!")
