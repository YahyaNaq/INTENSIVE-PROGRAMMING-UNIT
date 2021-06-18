# Python Program to Print an Inverted Star Pattern

star="*"
sp=2
for s in range(29,0,-4):
    print(star*s)
    print(" "*sp,end="")
    sp=sp+2
