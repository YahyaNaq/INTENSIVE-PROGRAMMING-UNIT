# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

str1="Yahya Faheem Naqvi"
count_word=1
count_chr=0
for i in str1:
    count_chr+=1
    if i==" ":
        count_word+=1
print(count_word, count_chr)
