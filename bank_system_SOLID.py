class Account:
    MIN_SAVING_BALANCE = 500

    def __init__(self, account_no, name, account_type, balance):
        self.account_no = account_no
        self.name = name
        self.account_type = account_type.upper()
        self.balance = balance

    def show_account(self):
        print("\n--- Account Details ---")
        print(f"Account No   : {self.account_no}")
        print(f"Account Name : {self.name}")
        print(f"Account Type : {self.account_type}")
        print(f"Balance      : {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self.account_type == "SAVING":
            self._withdraw_saving(amount)
        elif self.account_type == "CURRENT":
            self._withdraw_current(amount)
        else:
            raise ValueError("Invalid Account Type! Use SAVING or CURRENT")

    def _withdraw_saving(self, amount):
        if self.balance - amount < self.MIN_SAVING_BALANCE:
            raise Exception("Insufficient funds! Minimum balance must be 500")
        self.balance -= amount

    def _withdraw_current(self, amount):
        self.balance -= amount


# ---------------- MAIN PROGRAM ----------------

try:
    account_no = input("Enter Account Number: ")
    name = input("Enter Customer Name: ")
    account_type = input("Enter Account Type (SAVING/CURRENT): ")
    balance = float(input("Enter Balance: "))

    account = Account(account_no, name, account_type, balance)

    account.show_account()

    amount = float(input("\nEnter Amount to Withdraw: "))
    account.withdraw(amount)

    print("\nAfter Withdrawal:")
    account.show_account()

except Exception as e:
    print("Error:", e)
