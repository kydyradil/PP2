class Account:
    def __init__(self, owner, balance=0.0):
        """Constructor that initializes the account owner and balance"""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f" {amount} KZT has been deposited to {self.owner}'s account. New balance: {self.balance} KZT")
        else:
            print(" Deposit amount must be positive!")

    def withdraw(self, amount):
        """Method to withdraw money from the account, ensuring sufficient balance"""
        if amount > self.balance:
            print(f" Insufficient funds! Your balance: {self.balance} KZT")
        elif amount > 0:
            self.balance -= amount
            print(f" {amount} KZT has been withdrawn from {self.owner}'s account. New balance: {self.balance} KZT")
        else:
            print(" Withdrawal amount must be positive!")


owner_name = input("Enter account owner's name: ")
initial_balance = float(input("Enter initial balance: "))
account = Account(owner_name, initial_balance)


while True:
    action = input("\nChoose an action (deposit/withdraw/exit): ").lower()
    
    if action == "deposit":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif action == "withdraw":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif action == "exit":
        print(" Exiting the program. Your final balance:", account.balance, "KZT")
        break

    else:
        print(" Invalid command. Please enter 'deposit', 'withdraw', or 'exit'.")
