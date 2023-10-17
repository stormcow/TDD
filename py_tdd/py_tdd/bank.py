from .money import Money
from dataclasses import dataclass, field


@dataclass
class Bank:
    exchangeRates: dict[str, float] = field(default_factory=dict)

    def addExchangeRate(self, currencyFrom: str, currencyTo: str, rate: float) -> None:
        key = currencyFrom + "->" + currencyTo
        self.exchangeRates[key] = rate

    def convert(self, aMoney: Money, aCurrency: str) -> Money:
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)

        key = aMoney.currency + "->" + aCurrency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency)

        raise Exception(key)
