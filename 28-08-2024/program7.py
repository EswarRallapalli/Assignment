#Python program to convert lowercase vowel to uppercase in string.
str=(input("Enter the string: "))
vowels="aeiou"
for char in str:
    if char in vowels:
        upper_char = char.upper()
        str=str.replace(char,upper_char)
print("updated str: ",str)