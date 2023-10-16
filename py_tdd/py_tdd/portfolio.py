from dataclasses import dataclass, field
from .money import Money


@dataclass
class Portfolio:
    money: list[Money] = field(default_factory=list)

    def add(self, *moneys: Money) -> None:
        self.money.extend(moneys)

    def evaluate(self, currency: str) -> Money:
        total = 0.0
        for money in self.money:
            total += money.amount
        return Money(amount=total, currency=currency)
