#Python program to count the Occurrence Of Vowels & Consonants in a String.#
str=str(input("enter a string: "))
vowels=0
consonants=0
vowels1="aeiouAEIOU"
count=len(str)
for ch in str:
    if ch.isalpha():
      if ch in vowels1:
         vowels+=1
      else:
        consonants+=1

print("No of vowels: ",vowels)
print("No of consonants: ",consonants)

    







