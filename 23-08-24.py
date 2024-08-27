print("Welcome to ATM")

print("Plz insert Atm card")
banking =1000
pin=2345
option=True
balance=20000
amount=1000.0
pin=int(input("Enter your pin:" ))

if pin ==pin:
    print("Banking:")
    print("choose the option")


    while option:
        print("""
        1.Withdraw
        2.Ministatement
        3.deposit
        4.pin change""")
        break
    option=input("\n choose the option(1-4): ")
    if option=="1":
        print("\n withdraw")


        if option=='1':
            print("\n withdraw")
            amount= float(input("Enter the withdraw amount: "))

        if amount>0:
           if amount<=balance:
              balance -=amount
              print("your available amount is:", balance)

           else:
            print("Insufficiant funds.") 
        
            
        else:
         ("withdraw amonut must me positive")
         
             
            
                        
                        
    
    
    elif option=="2":
        print("\n Ministatement")
    elif option=="3":
        print("\n deposit")
        amount=float(input("Enter the amount to deposit: "))
        if amount>0:
           balance +=amount
           print("your amount deposit is successfully")
           print("your avaliable balance: ", balance)
        else:
           print("your amount not credited")
    
    elif option=="4":
        print("\n pin change")
        option=None
    else:
        print("\n exit")



           
           
elif pin==pin:

    print("incorrect pin")
else:
    print("Remove card")

