# Python Program to Print all the Prime Numbers within a Given Range

lower=int(input("Please enter lower range for prime numbers: "))
upper=int(input("Please enter upper range for prime numbers: "))
for num in range(lower,upper+1):
    if num>1:
        for div in range(2,num//2+1):
            if num%div==0:
                break
        else:
            print(num)
