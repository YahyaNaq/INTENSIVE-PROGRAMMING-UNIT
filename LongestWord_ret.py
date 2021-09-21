# Python Program to Read a List of Words and Return the Length of the Longest One

words=["abcde","b","c","ab","abc"]
len_Lword=len(words[0])
for i in range(1,len(words)):
    len_word=len(words[i])
    if len_word>len_Lword:
        len_Lword=len_word
print("Length of longest word is: ",len_Lword)
