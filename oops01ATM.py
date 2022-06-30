class Atm:
    #constructor
    def __init__(self):
        self.pin=""
        self.balance=0
        
        self.menu()
    def menu(self):
        user_input=input('''
Hello how would you like to proceed?
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. enter 5 to exit
''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        elif user_input=='5':
            self.exit()
    def create_pin(self):
        self.pin=input("enter pin\n")
        confirm_pin=input("confirm pin\n")
        if self.pin==confirm_pin:
            print("pin created succesfully")           
        else:
            print("pin and confirm pin is not matched")
    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount"))
            self.balance=self.balance+amount
            print("Amount added successfully")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount"))
            if self.balance>=amount:
                self.balance=self.balance-amount
                print("Amount withdraw successfully")
            else:
                print("Insufficient balance")
        else:
            print("wrong pin")
            self.menu()
    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print("Total Balance:",self.balance)
    def exit(self):
        print("bye")
        
# It is basic code of ATM 
            
            
            
            

