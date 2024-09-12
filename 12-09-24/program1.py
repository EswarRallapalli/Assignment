"""1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)"""

def t(data):
    res=[]
    for item in data:
        if isinstance(item,tuple):
            res.extend(t(item))
        else:
            res.append(item)
    return tuple(res)
data =(1,(1,2),(3,4,5))
print(t(data))      