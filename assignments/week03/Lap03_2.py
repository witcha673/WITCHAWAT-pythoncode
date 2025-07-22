#program ATM
print("welcome To KU ATM")
print("\n")

pin = input("enter pin: ")
bagmoney = 1000

if pin == "1234":
    while True:  
        print("\npin correct\n")
        print("1. Take out cash")
        print("2. Deposit")
        print("3. Exit")
        print("4.check is balance")

        action = input("choose menu number ")

        if action == "1":
            take1 = int(input("Enter money to withdraw "))
            bagmoney -= take1  
            print(f"You balance: {bagmoney} ")

        elif action == "2":
            take2 = int(input("Enter money to deposit "))
            bagmoney += take2  
            print(f"You balance {bagmoney} ")

        elif action == "3":
            print("You exit")
            break
        elif action == "4":
            print("You money balance {bagmoney}")   

        else:
            print("try again")

else:
    print("pin not correct")
