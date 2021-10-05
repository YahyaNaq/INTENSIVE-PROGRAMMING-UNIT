# Python Program to Remove the Characters of Odd Index Values in a String

string="0123456789"
even_str=""
for i in range(len(string)):
    if not(i%2):
        even_str+=string[i]
print("String without odd indexes:",even_str)
