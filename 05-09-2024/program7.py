#Write  a python program to sort dictionary by keys or values ?
dict={}
dict[5]="20"
dict[3]="40"
dict[4]="30"
dict[2]="10"
dict[1]="80"
print(dict)
key=sorted( dict.values())
key1=sorted(dict.keys())

print(key,key1)
