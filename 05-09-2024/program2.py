#Write a python program to check weather the given value is present in the dictionary or not ?
d={'name':"eswar",'phnnum':9154493289,'place':"vizag"}
i=str(input("enter a values: "))
#print(type(d))
if i in d.values():
    
     print("value exist",i)
     
else:
      print("Not exist",i)
print("")
