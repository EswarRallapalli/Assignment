"""count occurrence of the give in string"""
st="Rallapalli Eswar"
ch=input("Enter the character : ")
count =0
for i in st:
    if i == ch:
     count= count + 1
print((count))