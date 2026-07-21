class ATM:
    def __init__(self, balance=0.0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.is_authenticated = False

    def authenticate(self):
        print("=== ATM Authentication ===")
        for attempt in range(3):
            entered_pin = input("Enter your PIN: ").strip()
            if entered_pin == self.pin:
                self.is_authenticated = True
                print("PIN accepted. Welcome!\n")
                return True
            print("Invalid PIN. Try again.")
        print("Too many failed attempts. Session ended.")
        return False

    def show_menu(self):
        print("=== ATM Menu ===")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self):
        amount = self._prompt_amount("Enter deposit amount: ")
        if amount is None:
            return
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance:.2f}\n")

    def withdraw(self):
        amount = self._prompt_amount("Enter withdrawal amount: ")
        if amount is None:
            return
        if amount > self.balance:
            print("Insufficient funds. Please choose a smaller amount.\n")
            return
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance:.2f}\n")

    def _prompt_amount(self, prompt):
        raw_value = input(prompt).strip()
        try:
            amount = float(raw_value)
            if amount <= 0:
                print("Amount must be greater than zero.\n")
                return None
            return amount
        except ValueError:
            print("Invalid number. Please enter a valid amount.\n")
            return None

    def run(self):
        if not self.authenticate():
            return

        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()
            print()

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    atm = ATM(balance=500.00, pin="1234")
    atm.run()
