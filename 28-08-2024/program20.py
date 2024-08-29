#Python program to check given character is digit or not using isdigit() meth
str=input("enter a character: ")
num="1234567890"
if str in num:
    print(str,":its is a digit")
else:
    print(str,":its is not a digit")