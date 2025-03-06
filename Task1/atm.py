import getpass  # For secure PIN input
import datetime

class ATM:
    def __init__(self):
        # Initialize an empty dictionary to store account information.
        # Key: account_number (string), Value: {pin, balance, history}
        self.accounts = {}

    def create_account(self, account_number, pin, initial_balance=1000.0):
        # Check if the account number already exists.
        if account_number in self.accounts:
            return False  # Account already exists

        # Create a new account entry in the accounts dictionary.
        self.accounts[account_number] = {
            'pin': pin,  # Store the PIN directly (plain text - not recommended for real applications)
            'balance': initial_balance,  # Set the initial balance
            'history': []  # Initialize an empty transaction history list
        }
        # Add the initial deposit to the transaction history.
        self.accounts[account_number]['history'].append(f"Initial deposit: {initial_balance} at {datetime.datetime.now()}")
        return True

    def login(self, account_number, pin):
        # Check if the account number exists.
        if account_number not in self.accounts:
            return False
        # Verify the entered PIN against the stored PIN.
        if self.accounts[account_number]['pin'] == pin:
            return True
        return False

    def check_balance(self, account_number):
        # Return the account balance.
        return self.accounts[account_number]['balance']

    def deposit(self, account_number, amount):
        # Check if the deposit amount is valid.
        if amount <= 0:
            return False
        # Increase the account balance.
        self.accounts[account_number]['balance'] += amount
        # Add the deposit transaction to the history.
        self.accounts[account_number]['history'].append(f"Deposit: +{amount} at {datetime.datetime.now()}")
        return True

    def withdraw(self, account_number, amount):
        # Check if the withdrawal amount is valid and if there are sufficient funds.
        if amount <= 0 or amount > self.accounts[account_number]['balance']:
            return False
        # Decrease the account balance.
        self.accounts[account_number]['balance'] -= amount
        # Add the withdrawal transaction to the history.
        self.accounts[account_number]['history'].append(f"Withdrawal: -{amount} at {datetime.datetime.now()}")
        return True

    def change_pin(self, account_number, new_pin):
        # Change the account PIN.
        self.accounts[account_number]['pin'] = new_pin
        # Add the PIN change transaction to the history.
        self.accounts[account_number]['history'].append(f"PIN changed at {datetime.datetime.now()}")
        return True

    def transaction_history(self, account_number):
        # Return the transaction history list.
        return self.accounts[account_number]['history']

def main():
    # Create an ATM object.
    atm = ATM()

    while True:
        # Display the main menu.
        print("\nATM Machine")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        # Get the user's choice.
        choice = input("Enter choice: ")

        if choice == '1':  # Login
            # Get the account number and PIN.
            account_number = input("Enter account number: ")
            pin = getpass.getpass("Enter PIN: ")  # Use getpass for secure PIN input
            # Attempt to log in.
            if atm.login(account_number, pin):
                print("Login successful!")
                while True:  # Inner loop for logged-in user menu
                    # Display the logged-in user menu.
                    print("\nATM Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Logout")

                    # Get the user's menu choice.
                    menu_choice = input("Enter choice: ")

                    if menu_choice == '1':  # Check balance
                        print(f"Balance: {atm.check_balance(account_number)}")
                    elif menu_choice == '2':  # Deposit
                        amount = float(input("Enter deposit amount: "))
                        if atm.deposit(account_number, amount):
                            print("Deposit successful!")
                        else:
                            print("Invalid deposit amount.")
                    elif menu_choice == '3':  # Withdraw
                        amount = float(input("Enter withdrawal amount: "))
                        if atm.withdraw(account_number, amount):
                            print("Withdrawal successful!")
                        else:
                            print("Insufficient funds or invalid amount.")
                    elif menu_choice == '4':  # Change PIN
                        new_pin = getpass.getpass("Enter new PIN: ")
                        if atm.change_pin(account_number, new_pin):
                            print("PIN changed successfully!")
                    elif menu_choice == '5':  # Transaction history
                        history = atm.transaction_history(account_number)
                        for transaction in history:
                            print(transaction)
                    elif menu_choice == '6':  # Logout
                        break  # Exit the inner loop
                    else:
                        print("Invalid choice.")

            else:
                print("Invalid account number or PIN.")

        elif choice == '2':  # Create account
            # Get the new account number and PIN.
            account_number = input("Enter new account number: ")
            pin = getpass.getpass("Enter new PIN: ")
            # Attempt to create the account.
            if atm.create_account(account_number, pin):
                print("Account created successfully!")
            else:
                print("Account creation failed. Account number already exists.")

        elif choice == '3':  # Exit
            break  # Exit the outer loop

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
