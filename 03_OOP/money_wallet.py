"""Custom Wallet & Money Object
Demonstrates Magic/Dunder Methods (__init__, __str__, __repr__, __add__, __eq__, __len__, __getitem__).
"""

from typing import List, Union


class Money:
    """Represents a specific financial amount in a given currency."""

    CURRENCY_SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£"}

    def __init__(self, amount: Union[int, float], currency: str = "USD"):
        self.amount = round(float(amount), 2)
        self.currency = currency.upper()

    def __str__(self) -> str:
        """User-friendly string representation (e.g., '$25.50 USD')."""
        symbol = self.CURRENCY_SYMBOLS.get(self.currency, "")
        return f"{symbol}{self.amount:.2f} {self.currency}"

    def __repr__(self) -> str:
        """Developer/unambiguous representation for debugging."""
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __add__(self, other: "Money") -> "Money":
        """Overloads '+' operator: Allows Money + Money additions."""
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(
                f"Cannot add different currencies: '{self.currency}' and '{other.currency}'."
            )
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        """Overloads '==' operator: Checks if amounts and currencies match."""
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency


class Wallet:
    """Container holding multiple Money items."""

    def __init__(self, owner: str):
        self.owner = owner
        self.items: List[Money] = []

    def add_money(self, money: Money) -> None:
        """Adds a Money instance to the wallet."""
        self.items.append(money)
        print(f"[+] Added {money} to {self.owner}'s wallet.")

    def __len__(self) -> int:
        """Overloads len(wallet): Returns total number of money items."""
        return len(self.items)

    def __getitem__(self, index: int) -> Money:
        """Overloads wallet[index]: Allows direct indexing access."""
        return self.items[index]

    def total_balance(self, currency: str = "USD") -> Money:
        """Calculates total value for a target currency."""
        total = sum(item.amount for item in self.items if item.currency == currency)
        return Money(total, currency)


def main():
    print("--- 1. Testing Money Dunder Methods ---")
    m1 = Money(50.25, "USD")
    m2 = Money(24.75, "USD")
    m3 = Money(50.25, "USD")

    # __str__ and __repr__
    print(f"String representation (__str__):  {m1}")
    print(f"Developer repr (__repr__):       {repr(m1)}")

    # __add__
    combined = m1 + m2
    print(f"Addition result (m1 + m2):       {combined}")

    # __eq__
    print(f"Equality check (m1 == m3):       {m1 == m3}")
    print(f"Equality check (m1 == m2):       {m1 == m2}")

    print("\n--- 2. Testing Wallet Dunder Methods ---")
    my_wallet = Wallet("Alex")
    my_wallet.add_money(Money(20.00, "USD"))
    my_wallet.add_money(Money(50.00, "USD"))
    my_wallet.add_money(Money(15.00, "EUR"))

    # __len__
    print(f"\nItems in wallet (len(wallet)):   {len(my_wallet)}")

    # __getitem__
    print(f"First item in wallet (wallet[0]): {my_wallet[0]}")

    # Balance calculation
    print(f"Total USD Balance:               {my_wallet.total_balance('USD')}")


if __name__ == "__main__":
    main()
