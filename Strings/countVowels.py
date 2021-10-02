# Python Program to Count the Number of Vowels in a String

name=input("Please input your string: ")
num_vowel=0
vowels=["a","e","i","o","u"]
for n in range(5):
    if vowels[n] in name:
        num_vowel+=1
print("Number of vowels in the string are:",num_vowel)
