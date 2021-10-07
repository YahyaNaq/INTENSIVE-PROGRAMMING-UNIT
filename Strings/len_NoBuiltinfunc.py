# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1=input("Please input your string: ")
str2=input("Please input your string: ")

len1=0
while str1[-1]!=str1[len1]:
    len1+=1

len2=0
while str2[-1]!=str2[len2]:
    len2+=1

if len1>len2:
    print("Larger string:",str1)
if len2>len1:
    print("Larger string:",str2)
if len1==len2:
    print("Both strings have equal length!")
