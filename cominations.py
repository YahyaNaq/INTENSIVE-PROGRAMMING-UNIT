# Python Program to accept three digits and Print all possible combinations of the digits

lst=[]
for i in range(3):
    n=int(input("Enter:"))
    lst.append(n)
for i in lst:
    comb=str(i)
    for j in lst:
        if i!=j:
            comb+=str(j)
    print(comb)
    comb=str(i)
    for j in lst[::-1]:
        if i!=j:
            comb+=str(j)
    print(comb)
