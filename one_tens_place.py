# Python Program to form an integer that has the number of digits at ten's place
# and the least significant digit of the entered integer at one's place

int_=int(input("Please enter an integer: "))
last=int_%10
count=0
for i in range(int_):
    int_//=10
    count+=1
    if int_==0:
        break
        
num=str(count)+str(last)
print(num)
