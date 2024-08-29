#Python program to remove repeated character from string#
str=str(input("enter a string: "))
x=""
for ch in str:
    if ch not in x:
        x= x+ch
print(x)  
