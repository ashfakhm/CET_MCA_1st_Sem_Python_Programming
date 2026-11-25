"""Create a bank account and perform deposit and withdrawal operations."""


class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def display(self):
        print("Account number:", self.account_number)
        print("Name:", self.name)
        print("Account type:", self.account_type)
        print("Balance:", self.balance)


account = BankAccount(
    input("Enter account number: "),
    input("Enter account holder name: "),
    input("Enter account type: "),
    float(input("Enter opening balance: ")),
)

deposit_amount = float(input("Enter amount to deposit: "))
if account.deposit(deposit_amount):
    print("Deposit successful.")
else:
    print("Deposit amount must be greater than zero.")

withdrawal_amount = float(input("Enter amount to withdraw: "))
if withdrawal_amount <= 0:
    print("Withdrawal amount must be greater than zero.")
elif account.withdraw(withdrawal_amount):
    print("Withdrawal successful.")
else:
    print("Insufficient balance.")

account.display()
