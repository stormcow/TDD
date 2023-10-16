from dataclasses import dataclass, field
from .money import Money


@dataclass
class Portfolio:
    money: list[Money] = field(default_factory=list)

    def add(self, *moneys: Money) -> None:
        self.money.extend(moneys)

    @staticmethod
    def __convert(money: Money, currency: str) -> float:
        eurToUsd = 1.2
        if money.currency == currency:
            return money.amount
        return money.amount * eurToUsd

    def evaluate(self, currency: str) -> Money:
        total = 0.0
        for money in self.money:
            total += self.__convert(money, currency)
        return Money(amount=total, currency=currency)
