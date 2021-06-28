# Python Program to Print Largest Even and Largest Odd Number in a List

lst=[4,2,5,3,1,8,10,6,7,15]
even=0
odd=0
for i in lst:
    if i%2==0 and i>even:
        even=i
    if i%2==1 and i>odd:
        odd=i
print(f"largest even:{even}; largest odd:{odd}")
