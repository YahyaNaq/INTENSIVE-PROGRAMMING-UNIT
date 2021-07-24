# Python Program to Find the Sum of First N Natural Numbers

N=int(input("Please enter a natural number: "))
Sum_to_N=0
for n in range(1,N+1):
    Sum_to_N+=n
print("Sum to first {} natural numbers is {}".format(N,Sum_to_N))
