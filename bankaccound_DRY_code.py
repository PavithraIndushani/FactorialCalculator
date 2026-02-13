class BankAccount:
    def __init__(self, account_no, account_name, account_type, balance):
        self.account_no = account_no
        self.account_name = account_name
        self.account_type = account_type.upper()
        self.balance = balance

    def show_account(self):
        print(f"""
Account No   : {self.account_no}
Account Name : {self.account_name}
Account Type : {self.account_type}
Balance      : {self.balance}
""")

    def withdraw(self, amount):
        if self.account_type not in ["SAVING", "CURRENT"]:
            raise Exception("Invalid Option, Please enter SAVING/CURRENT")

        new_balance = self.balance - amount

        # Minimum balance check only for SAVING
        if self.account_type == "SAVING" and new_balance < 500:
            raise Exception("Insufficient Fund !! Cannot withdraw money")

        self.balance = new_balance
        return self.balance


# -------- Main Program --------
account_no = input("Enter Account Number : ")
account_name = input("Enter Customer Name : ")
account_type = input("Enter Account Type (SAVING/CURRENT) : ")
balance = float(input("Enter Balance : "))

account = BankAccount(account_no, account_name, account_type, balance)

account.show_account()

amount = float(input("Enter Amount to be Withdrawn : "))
try:
    account.withdraw(amount)
    print("\nAfter withdraw new balance :")
    print("Balance :", account.balance)
except Exception as e:
    print("Error:", e)
