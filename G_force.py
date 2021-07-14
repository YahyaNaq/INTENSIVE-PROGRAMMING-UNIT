# Python Program to Find the Gravitational Force Acting Between Two Objects

m1=float(input("Please enter the mass of first object:"))
m2=float(input("Please enter the mass of second object:"))
r=float(input("Please enter distance between radii of two objects: "))
G=6.67408*10**-11
F=G*m1*m2/r**2
print("Gravitational force acting between two objects is",F)
