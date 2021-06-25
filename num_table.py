# Python Program to Print Table of a Given Number

num=eval(input("Please enter a number: "))
for factor in range(1,11):
    print("{} x {} = {}".format(num,factor,num*factor))
