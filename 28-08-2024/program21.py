#Python program to calculate sum of integers in string#
str=str(input("enter a string: "))
x="1234567890"
num=0
for ch in str:
    if ch in x:
        num+=int(ch)
print("sum of intergers in string:- ",num)