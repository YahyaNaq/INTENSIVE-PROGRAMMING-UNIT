# Python Program to compute prime factors of an integer

int_=int(input("Please enter an integer: "))
lst=[]
for i in range(2,int_+1):
    if int_%i==0:
        lst.append(i)
for i in lst:
    bool_=1
    for j in range(2,i//2+1):
        if i%j==0:
            bool_=0
            break
    if bool_:
        print(i)
