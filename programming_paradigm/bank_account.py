class BankAccount:
    """
    A class to represent a simple bank account.
    Manages account balance, deposits, and withdrawals.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account.
                                               Defaults to 0.0.
        """
        # Encapsulate the account balance
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.__account_balance += amount
            # No return value needed as per problem description, but a print is good for feedback
            # print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds or invalid amount).
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif self.__account_balance >= amount:
            self.__account_balance -= amount
            # print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            # print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

