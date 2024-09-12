"""Write a Python program to sort a tuple of tuples based on the second element
of each tuple.
Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))"""

def second(tul): 
    tul.sort(key = lambda x: x[1]) 
    return tul 
tul= [('eswar', 1), ('sunny', 5), ('naveen', 2),('praveer', 6)]
print(second(tul))