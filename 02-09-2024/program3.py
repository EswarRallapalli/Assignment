#write a python program to add an item to the tuple ?#
t=(1,"a",5.53,4,5,"hello")
#using "+" operater#
t=t+(True,)
print(t)
#converting into list
l=list(t)
l.append(7)
t=tuple(l)
print(l)
print(t)
