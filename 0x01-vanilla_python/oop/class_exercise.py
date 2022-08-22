"""
Write a program to simulate banking operations by a bank customer

Define Custom class
Simulate bank deposits
Simulate bank withdraws (check that you have enough balance amount)
print receipt
"""
import string


class InsufficientFund(Exception):
    pass


class BankAccount:
    def __init__(self, name: str, phone: str, balance: float, pin: str) -> None:
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self._balance = balance
        self.name = name
        self.phone = phone
        self.pin = pin

    def __str__(self):
        return (
            f"Account Details:\n"
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Balance: {self.balance}\n"
        )

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The withdrawal amount must be more than 0")

        if amount > self._balance:
            raise InsufficientFund("Insufficient ammount for withdrawal")

        self._balance -= amount


if __name__ == "__main__":
    account1 = BankAccount(
        "Annet Allen", "+2567809090303", 20000, "{string.digits[1:6]}"
    )
    account2 = BankAccount(
        "Derrick Smith", "+256780030303", 30000, "{string.digits[5:]}"
    )
    print(account1)
    account1.deposit(100000000)
    print(account1)

    account1.withdraw(500000)
    print(account1)

    print(account2)
    account2.deposit(300000000)
    print(account2)

    account2.withdraw(4050000)
    print(account2)
