#Python Program to print all numbers in a range divisible by a given number
den=eval(input("Please enter a number: "))
num=eval(input("Please enter the maximum number you want to check: "))
for i in range(num+1):
    if i>=den:
        if not(i%den):
            print(i)
