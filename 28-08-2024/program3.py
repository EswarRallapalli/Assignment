#Given string is Palindrome or not .................
pl=str(input("Enter the word: "))
if pl==pl[::-1]:
   print("its is a palindrome")
else:
   print("Its not a palindrome ")