# Python Program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes

nums=list()
lower=int(input("Please enter lower range for prime numbers: "))
upper=int(input("Please enter upper range for prime numbers: "))
for l in range(lower,upper+1):
    nums.append(l)
    if l==1:
        nums.remove(l)
for d in nums:
    for e in nums:
        if not(e%d) and e>d and d>1:
            nums.remove(e)
print("\nPrime numbers using Sieve of Eratosthenes:",nums)
