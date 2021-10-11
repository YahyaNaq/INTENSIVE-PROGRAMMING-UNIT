# Python Program to Count Number of Lowercase Characters in a String

name=input("Please input your string: ")
lower_n=0
lower="abcdefghijklmnopqrstuvwxyz"
for i in name:
    if i in lower:
        lower_n+=1
print("Number of LOWER case letters:",lower_n)
