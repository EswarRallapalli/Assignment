# check if two Strings are Anagram
word1 =str(input("Enter the word1"))
word2=str(input("Enter the word2"))
if (sorted(word1)==sorted(word2)):
   print("its is anagram")
else:
   print("its not a anagram")