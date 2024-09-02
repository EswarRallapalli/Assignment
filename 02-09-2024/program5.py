#Write a python program to find most frequent element in tuple ?
t=(30,40,80,30,60,27)
count=0
r=t[0]
for ele in t:
    freq=t.count(ele)
    if(freq>count):
        count=freq
        r=ele
print(r)


