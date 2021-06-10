# Python Program to find the sum of digits in a number
# *** This program is valid upto to 5 digit numbers ***

num=int(input("Please input a number: "))
if num>9 and num<100:
    Sum=num//10+num%10
    print("Sum of digits of the given number is:",Sum)
if num>99 and num<1000:
    Sum=num//100+(num%100)//10+(num%100%10)
    print("Sum of digits of the given number is:",Sum)
if num>999 and num<10000:
    Sum=num//1000+(num%1000)//100+(num%1000%100)//10+(num%1000%100%10)
    print("Sum of digits of the given number is:",Sum)
