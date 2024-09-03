"""Write a program that computes the net amount of a bank account based a transaction
log from console input.The transaction log format is shown as following: D 100 W 200 D 
means deposit while W means withdrawal. Suppose the following input is supplied to the
program: D 300 D 300 W 200 D 100 Then, the output should be: 500
"""
total = 0
while True:
    deposit= input()
    if deposit == "":
        break
    else:
        deposit = deposit.split(" ")
        if deposit[0] == "D":
            total = total + int(deposit[1])
        elif deposit[0] == "W":
            total = total - int(deposit[1])

print(total)

