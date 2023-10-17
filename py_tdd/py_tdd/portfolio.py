from dataclasses import dataclass, field
from .money import Money
from .bank import Bank


@dataclass
class Portfolio:
    money: list[Money] = field(default_factory=list)

    def add(self, *moneys: Money) -> None:
        self.money.extend(moneys)

    def evaluate(self, bank: Bank, currency: str) -> Money:
        total = 0.0
        failures: list[Exception] = []
        for m in self.money:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)
        if len(failures) == 0:
            return Money(amount=total, currency=currency)
        failureMessage = ",".join(str(f) for f in failures).replace("'", "")
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")
