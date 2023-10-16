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
        failures: list[KeyError] = []
        for m in self.money:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)
        if len(failures) == 0:
            return Money(amount=total, currency=currency)
        failureMessage = ",".join(str(f) for f in failures).replace("'","")
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")
