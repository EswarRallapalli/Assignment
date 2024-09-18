"""Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. 
python # Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)"""
def t(data):
    res=[]
    for item in data:
        if isinstance(item,tuple):
            res.extend(t(item))
        else:
            res.append(item)
    return tuple(res)
data =eval(input("enter the tuple: "))
print(t(data))      