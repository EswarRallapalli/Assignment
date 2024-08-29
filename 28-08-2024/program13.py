#Python program to check given character is vowel or consonant"#
str=str(input("enter a character: "))
vowels="aeiou"
vowels1="AEIOU"

if str in vowels:
    print(str,":its is a vowel")
elif str in vowels1:
    print(str,":its is a vowel")
else:
    print(str,":it is a consonant")

