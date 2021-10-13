# Python Program to Check if a String is a Palindrome or Not

string=input("Please enter a string: ").lower()
ind=-1
for i in range(len(string)//2):
    print(string[ind],string[i])
    
    if string[i]==string[ind]:
        ind+=-1
    else:
        break
if len(string)//2==-(ind+1):
    print("Your string is a palindrome!")
else:
    print("Sorry!")
