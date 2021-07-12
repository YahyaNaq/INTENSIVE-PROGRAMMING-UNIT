# Python Program to Find the Area of a Triangle Given All Three Sides

from math import *
side1=int(input("Please input length of first side: "))
side2=int(input("Please input length of second side: "))
side3=int(input("Please input length of third side: "))
s=(side1+side2+side3)/2
Area=sqrt(s*(s-side1)*(s-side2)*(s-side3))
print("Area of triangle is {} sq units".format(Area))
