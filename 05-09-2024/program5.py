#Write a python program to combine two dictionaries by adding values of common keys?
Dict1={'a':20,'b':30,'c':40}
Dict2={'a':30,'b':40,'c':30}
for i in Dict2:
    if i in Dict1:
     Dict2[i]=Dict2[i]+Dict2[i]
    
print(Dict2)
