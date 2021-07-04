# Python Program to Check if a Number is an Armstrong Number

sum_cubes=0
arm_n=input("Please enter a number: ")
arm_n_int=int(arm_n)
for n in arm_n:
    sum_cubes+=int(n)**3
if sum_cubes==arm_n_int:
    print("Yes",arm_n,"is an armstrong number!")
else:
    print("Sorry!")
