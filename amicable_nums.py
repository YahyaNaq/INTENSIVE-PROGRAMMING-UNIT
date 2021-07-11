# Python Program to Check If Two Numbers are Amicable Numbers

n1=int(input("Please input 1st number: "))
n2=int(input("Please input 2nd number: "))
sumn1=0
sumn2=0
for i in range(1,n1//2+1):
    if n1%i==0:
        sumn1+=i
for i in range(1,n2//2+1):
    if n2%i==0:
        sumn2+=i
if n1==sumn2 and n2==sumn1:
    print("YES, given numbers are amicable numbers!")
else:
    print("SORRY, given numbers aren't amicable numbers!")
