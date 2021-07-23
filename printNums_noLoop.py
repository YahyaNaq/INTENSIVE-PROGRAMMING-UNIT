# Python Program to Print Numbers in a Range (1,upper) Without Using any Loops

def range(f, a):
    print(f)
    f+=1
    if f!=a+1:
        range(f,a)
range(1,10)
