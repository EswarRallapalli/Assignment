#Python program to print all non repeating character in string#
str=str(input("enter a string: "))
for ch in str:
    if str.count(ch)<2:
        print(ch)
