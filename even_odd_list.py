# Python Program to Put Even and Odd elements in a List into Two Different Lists

lst=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in lst:
    if i%2:
        odd.append(i)
    else:
        even.append(i)
print("Even: {}\nOdd: {}".format(even,odd))
