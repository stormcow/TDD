from dataclasses import dataclass


@dataclass
class Money:
    amount: float
    currency: str

    def times(self, multiplier: int) -> "Money":
        return Money(amount=self.amount * multiplier, currency=self.currency)

    def divide(self, divisor: int) -> "Money":
        return Money(amount=self.amount / divisor, currency=self.currency)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:0.2f}"
