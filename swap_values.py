#Python Program to Exchange the Values of Two Numbers WithoutUsing a Temporary Variable

val1=eval(input("Please enter first value: "))
val2=eval(input("Please enter second value: "))
val1,val2=val2,val1
print("val1:{} val2:{}".format(val1,val2))
