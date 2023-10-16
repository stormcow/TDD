from dataclasses import dataclass, field
from .money import Money


@dataclass
class Portfolio:
    money: list[Money] = field(default_factory=list)

    def add(self, *moneys: Money) -> None:
        self.money.extend(moneys)

    @staticmethod
    def __convert(money: Money, currency: str) -> float:
        exchangeRates = {"EUR->USD": 1.2, "USD->KRW": 1100}
        if money.currency == currency:
            return money.amount
        key = money.currency + "->" + currency
        return money.amount * exchangeRates[key]

    def evaluate(self, currency: str) -> Money:
        total = 0.0
        for money in self.money:
            total += self.__convert(money, currency)
        return Money(amount=total, currency=currency)
