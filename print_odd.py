# Python Program to print odd numbers within a given range

print("This program will print odd numbers in a given range.")
Range=int(input("Please enter the range: "))
print("Odd numbers are:")
for num in range(Range):
    if num%2:
        print(num)
