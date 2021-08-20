# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

lst_tuple=[]
num=int(input("Please input a number to add in list of tuples: "))
lst_tuple.append((num,num**2))
Ques=input("Do you want to add another tuple in the list? ")
while Ques=="yes" or Ques=="Yes" or Ques=="YES" or Ques=="Y" or Ques=="y":
    num=int(input("Please input a number to add in list of tuples: "))
    lst_tuple.append((num,num**2))
    Ques=input("Do you want to add another tuple in the list? ")
print(lst_tuple)
