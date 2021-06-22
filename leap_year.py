# Python Program to Check Whether a Given Year is a Leap Year

year=int(input("Please enter an year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Your entered year is a leap year!")
else:
    print("Your entered year is not a leap year!")
