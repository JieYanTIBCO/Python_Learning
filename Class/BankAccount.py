import utils.setup_logging as sl
import logging
import datetime

sl.setup_logging()


class BankAccount:

    # initial function

    def __init__(self, account_holder, balance, transaction_history):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f"Bank account created for {self.account_holder}")

    # deposit function
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            now = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
            self.transaction_history.append(f"{now}:{
                                            self.account_holder} deposit {amount}. And current balance is {self.balance}")
        else:
            raise Exception(f" the mount is not a validate value")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0 and self.balance >= amount:
            self.balance -= amount
            now = datetime.datetime.now().isoformat(sep=" ", timespec="milliseconds")
            self.transaction_history.append(f"{now}:{
                self.account_holder} withdraw {amount}. And current balance is {self.balance}")
        elif self.balance < amount:
            raise Exception(
                f"your account does not have enough money for this transaction!")
        else:
            raise Exception(f"withdraw transaction is failed!")

    def print_balance(self):
        self.logger.info(self.balance)

    def print_transaction_history(self):
        self.logger.info("\n".join(self.transaction_history))


logger = logging.getLogger(__name__)

account1 = BankAccount("Jackie", 400, "")

account1.deposit(100)

account1.withdraw(200)
account1.deposit(300)
account1.print_balance()
account1.print_transaction_history()
