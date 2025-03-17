# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200

# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

# Custom exception class (optional, for clarity)
import json


class InvalidTransactionError(Exception):
    """
    Custom exception raised when a transaction is invalid.
    """

    def __init__(self, message, account_name=None, operation=None, amount=None):
        super().__init__(message)
        self.account_name = account_name
        self.operation = operation
        self.amount = amount

    def __str__(self):
        base_message = super().__str__()
        details = []
        if self.account_name:
            details.append(f"Account: {self.account_name}")
        if self.operation:
            details.append(f"Operation: {self.operation}")
        if self.amount is not None:
            details.append(f"Amount: {self.amount}")
        details_message = ", ".join(details)
        return (
            f"{base_message}. Details: {details_message}" if details else base_message
        )


# Define a function for validation


def validate_transaction_line(line):
    """Validate the structure and format of a transaction line."""
    # Remove leading and trailing spaces
    line = line.strip()

    # Split the line into components
    parts = line.split()

    # Validate the number of components
    if len(parts) != 3:
        raise InvalidTransactionError(
            f"Invalid transaction line format: '{
                                      line}'. Expected 3 components."
        )

    account_name, operation, amount = parts

    # Validate operation type
    if operation not in {"D", "W"}:
        raise InvalidTransactionError(
            f"Invalid operation type: {
                operation}. Must be 'D' (Deposit) or 'W' (Withdrawal)."
        )

    # Validate amount
    try:
        amount = int(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        raise InvalidTransactionError(
            f"Invalid amount: {amount}. Must be a positive integer."
        )

    return account_name, operation, amount


# account_name operation amount


def balance(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        account_balance = {}
        # processing transaction lines
        for line in lines:
            try:
                # Call the validation line function to validate account_name, operation, amount and return it back.
                account_name, operation, amount = validate_transaction_line(line)

                # Proceed with transaction processing
                # if account_name is not in the dictionary, set initialed amount
                if account_name not in account_balance:
                    account_balance[account_name] = 0

                    # set balance based on operations and make sure balance is not less than 0
                if operation == "D":
                    account_balance[account_name] += amount
                else:  # operation has already been checked either D or W
                    if account_balance[account_name] < amount:
                        raise InvalidTransactionError(
                            f"Invalid Transaction: account_name={
                                account_name}, operation={operation}, amount={amount}. "
                            "Balance must be greater than amount during withdrawal. Transaction cancelled."
                        )
                    # deduct from balance
                    account_balance[account_name] -= amount

            except InvalidTransactionError as e:
                # Handle the validation error
                print(e)

    return account_balance


account_balance = balance("./Python_Learning/100_Python_challenging/transactions.log")

print(json.dumps(account_balance, indent=4))
