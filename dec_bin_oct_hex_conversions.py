#Python Program to Convert Decimal to Binary, Octal and Hexadecimaland vice versa without using built in functions

n=int(input("Please enter the number you want to convert: "))

#Decimal to Binary
quo=n//2
rem=n%2
Bin=str(rem)
while quo>1:
    rem=quo%2
    Bin=str(rem)+Bin
    quo=quo//2
Bin=str(quo)+Bin
print("Binary:", Bin)

#Decimal to Octal
Q=n//8 
R=n%8
Oct=str(R)
while Q>0:
    R=Q%8
    Oct=str(R)+Oct
    Q=Q//8
print("Octal:",Oct)

#Decimal to Hexadecimal
Q=n//16
R=n%16
Hex=str(R)
while Q>0:
    R=Q%16
    Hex=str(R)+Hex
    Q=Q//16
print("Hexadecimal:",Hex)
