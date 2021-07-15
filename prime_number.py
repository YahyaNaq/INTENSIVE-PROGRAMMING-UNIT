# Python Program to Check if a Number is a Prime Number

num=int(input("Please enter a number: "))
bool_=1
if num!=1:    
    for i in range(2,num//2+1):
        if num%i==0:
            print("Not a prime number!")
            bool_=0
            break
    if bool_:
        print("Yes! A prime number!")
else:
    print("Not a prime number!")
