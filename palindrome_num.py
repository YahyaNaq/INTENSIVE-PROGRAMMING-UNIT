# Python Program to check if a number is a Palindrome
# !!! Take input as an integer !!!

num=int(input("Please input a number: "))

if num>999 and num<10000:
    rev_n=int(str(num%10)+str((num%100)//10)+str((num%1000)//100)+str(num//1000))
    if num==rev_n:
        print("Entered number is palindrome!")
    else:
        print("Sorry!")
        
if num>9999 and num<100000:
    rev_n=int(str(num%10)+str((num%100)//10)+str((num%1000)//100)+str(num%10000//1000)+str(num//10000))
    if num==rev_n:
        print("Entered number is palindrome!")
    else:
        print("Sorry!")
        
if num>99999 and num<1000000:
    rev_n=int(str(num%10)+str((num%100)//10)+str((num%1000)//100)+str(num%10000//1000)+str(num%100000//10000)+str(num//100000))
    if num==rev_n:
        print("Entered number is palindrome!")
    else:
        print("Sorry!")
