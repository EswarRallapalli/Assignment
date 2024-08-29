#Python program to count alphabets, digits and special characters.\
str=str(input("enter a string:"))
alph=0
digits=0
spl=0
for ch in range(len(str)):
    if(str[ch].isalpha()):
        alph=alph+1
    elif(str[ch].isdigit()):
        digits=g=digits+1
    else:
        spl=spl+1
print("No of alphabets:- ",alph)
print("NO Of digits:- ",digits)
print("no of special character:-",spl)
        

