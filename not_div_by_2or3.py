# Python Program to print all integers that aren't divisible by 2 or3 & lie between 1 & 50

print("Integers that aren't divisible by 2 or 3 and lie between 1 and 50 are: ")
for i in range(1,50):
    if i%2 and i%3:
        print(i)
