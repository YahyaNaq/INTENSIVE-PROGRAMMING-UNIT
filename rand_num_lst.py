# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List

from random import randint
Random=list()
n=int(input("How many numbers do you want to append: "))
for i in range(n):
    index=randint(1,20)
    Random.append(index)
print(Random)
