#Write a python proram to convert tuple into a string ?#
t=("we",2,7.8,True)
s=''
for ele in t:
    s+=str(ele)
print(s)
print(type(s))
