# Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

name=input("Please input your string: ")
lower_n=0
lower="abcdefghijklmnopqrstuvwxyz"
upper_n=0
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in name:
    if i in lower:
        lower_n+=1
    if i in upper:
        upper_n+=1
print("Number of LOWER case letters:",lower_n)
print("Number of UPPER case letters:",upper_n)
