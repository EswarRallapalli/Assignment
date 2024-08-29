#Python program to delete vowels in a given string.#
str=str(input("enter a string: "))
vowels="aeiouAEIOU"
ans=""

for ch in str:
    if ch not in vowels:
        ans +=ch
print("After delete vowels: ",ans)        

    
