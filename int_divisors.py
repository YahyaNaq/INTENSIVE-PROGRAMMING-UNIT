# Python Program to Generate all the Divisors of an Integer

Int=int(input("Please enter an integer: "))
print("Divisors of the given integer are:")
for div in range(1,Int):
    if not(Int%div):
        print(div)
