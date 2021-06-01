rev_n=int(input("Please input a non-singular digit number: "))
if rev_n>9 and rev_n<100:
    dDigrev_n=str(rev_n%10)+str(rev_n//10)
    print("Reversed number:",dDigrev_n)
if rev_n>99 and rev_n<1000:
    tDigrev_n=str(rev_n%10)+str((rev_n%100)//10)+str(rev_n//100)
    print("Reversed number:",tDigrev_n)
if rev_n>999 and rev_n<10000:
    qDigrev_n=str(rev_n%10)+str((rev_n%100)//10)+str((rev_n%1000)//100)+str(rev_n//1000)
    print("Reversed number:",qDigrev_n)