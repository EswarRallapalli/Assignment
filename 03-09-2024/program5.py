"""5.Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3"""
str=str(input("enter a  string: "))
digits=0
alph=0
for ch in range(len(str)):

    if(str[ch].isalpha()):
        alph=alph+1
    elif(str[ch].isdigit()):
        digits=digits+1
print("letter:",alph ,"digits:",digits)




       