"""4.Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,worldo"""
input=str(input("enter a string"))
l=input.split(',')
l.sort()
print((',').join(l))