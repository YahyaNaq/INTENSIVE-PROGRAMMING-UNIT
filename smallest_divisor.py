# Write Python Program to Find the Smallest Divisor of an Integer

Int=int(input("Please enter an integer: "))
for sdiv in range(2,Int+1):
    if not(Int%sdiv):
        break
print("Smallest divisor of the given integer: ",sdiv)
