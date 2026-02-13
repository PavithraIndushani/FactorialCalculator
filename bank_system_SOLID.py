def show_account(account_no, account_name, account_type, balance):
    print("\n------ Account Details ------")
    print(f"Account No   : {account_no}")
    print(f"Account Name : {account_name}")
    print(f"Account Type : {account_type}")
    print(f"Balance      : {balance:.2f}")


def withdraw(account_type, balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0.")

    account_type = account_type.upper()

    if account_type == "SAVING":
        if balance - amount < 500:
            raise ValueError("Insufficient funds! Minimum balance of 500 required for SAVING account.")
        return balance - amount

    elif account_type == "CURRENT":
        return balance - amount

    else:
        raise ValueError("Invalid account type! Please enter SAVING or CURRENT.")


def main():
    
    try:
        account_no = input("Enter Account Number : ")
        account_name = input("Enter Customer Name : ")
        account_type = input("Enter Account Type (SAVING/CURRENT) : ")
        balance = float(input("Enter Balance : "))

        show_account(account_no, account_name, account_type, balance)

        amount = float(input("\nEnter Amount to Withdraw : "))
        balance = withdraw(account_type, balance, amount)

        print("\nWithdrawal Successful!")
        print(f"Updated Balance : {balance:.2f}")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
