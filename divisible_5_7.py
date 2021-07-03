# Python Program to Find Those Numbers which are Divisible by 7
# and Multiple of 5 in a Given Range of Numbers

Range=int(input("Please enter a range:"))
print("Numbers divisible by 5 & 7 within the given range are: ")
for i in range(1,Range+1):
    if not(i%5) and not(i%7):
        print(i)
