"""Step 10, on the side: nobody can bypass the rules, and errors say which.

uv run python B4/side/e10_bank.py
"""


# A family of errors: a caller can catch them all (BankError) or one of them.
class BankError(Exception):
    """Every error of this module."""


class UnknownAccountError(BankError):
    pass


class RefusedError(BankError):
    pass


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0  # "_": not for the outside, use the methods
        self._history: list[int] = []

    @property
    def balance(self) -> int:
        """Read-only: there is no setter, `account.balance = 10**6` fails."""
        return self._balance

    @property
    def history(self) -> list[int]:
        """A copy: appending to it changes nothing in the account."""
        return list(self._history)

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise RefusedError(f"A deposit must be positive, got {amount}.")
        self._balance += amount
        self._history.append(amount)

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise RefusedError(f"{self.owner} has only {self._balance} EUR.")
        self._balance -= amount
        self._history.append(-amount)


class Bank:
    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def open(self, owner: str) -> Account:
        account = Account(owner)
        self._accounts[owner.lower()] = account
        return account

    def get(self, owner: str) -> Account:
        if owner.lower() not in self._accounts:
            raise UnknownAccountError(f"No account for {owner}.")
        return self._accounts[owner.lower()]


if __name__ == "__main__":
    bank = Bank()
    account = bank.open("Lou")
    account.deposit(50)
    account.history.append(1_000_000)  # changes a copy, not the account
    print(account.balance, account.history)
    try:
        account.balance = 1_000_000
    except AttributeError as error:
        print(f"AttributeError: {error}")
    for action in [lambda: account.withdraw(80), lambda: bank.get("Zoé")]:
        try:
            action()
        except BankError as error:  # one except for the whole family
            print(f"{type(error).__name__}: {error}")
