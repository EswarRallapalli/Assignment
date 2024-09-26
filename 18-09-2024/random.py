import random
for i in range(1): 
     print("enter numder 1 to 50")
     random_number = random.randint(1,50)
     user_number  = int(input("Enter the number: "))
     if random_number==user_number:
         print(user_number,"congrats you have won the game","Random number:",random_number)
     elif user_number>50:
      print(user_number,"sorry,you entered a wrong nunmber")
     else:
         print(user_number,":sorry you lost game","Random number:",random_number)
         
 