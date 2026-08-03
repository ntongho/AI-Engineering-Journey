# Create a class:
# BankAccount

# Attributes:
# owner
# balance

# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()

# Rules:
# Balance cannot become negative.
# If withdrawal exceeds the balance:
# Insufficient funds.
# Otherwise update the balance.


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        """Initializes the bank account with an owner and an initial balance."""
        self.owner = owner
        # Ensures that the initial balance itself cannot be negative
        self.balance = max(0.0, balance)

    def deposit(self, amount: float):
        """Increases the balance by the specified amount."""
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float):
        """Decreases the balance if funds are sufficient, otherwise blocks it."""
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")

    def display_balance(self):
        """Prints the current balance of the account."""
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:.2f}")
