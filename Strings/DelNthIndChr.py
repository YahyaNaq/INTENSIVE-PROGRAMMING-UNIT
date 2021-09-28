# Python Program to Remove the nth Index Character from a Non-Empty String

name="Yahya Faheem Naqvi"
name1=""
for i in range(len(name)):
    if i==1:
        continue
    else:
        name1+=name[i]
    
print(name1)

           #OR
    
name1=name[0]+name[2:]
print(name1)
