"""Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
"""
str=str(input("enter a  string: "))
upper=0
lower=0
for ch in range(len(str)):

    if(str[ch].isupper()):
        upper=upper+1
    elif(str[ch].islower()):
        lower=lower+1
print("Upper case:",upper ,"lower case:",lower)