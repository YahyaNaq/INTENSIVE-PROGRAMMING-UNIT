# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

name="phone"
new_str=name[1:-1]
print(new_str)
new_str=name[-1]+new_str+name[0]
print("New string:",new_str)
