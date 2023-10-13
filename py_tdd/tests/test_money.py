import unittest
from dataclasses import dataclass, field


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
<<<<<<< HEAD


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
=======
>>>>>>> 8b41058510cc343105eedc07d1466d8040fc1b19


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self) -> None:
        fiveDollars = Money(5, "USD")
        tenDollars = fiveDollars.times(2)
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self) -> None:
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self) -> None:
        originalMoney = Money(4002, "KRW")
        expectedMoney = Money(1000.5, "KRW")
<<<<<<< HEAD
        self.assertEqual(expectedMoney, originalMoney.divide(4))

    def testAddition(self) -> None:
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))
=======
        self.assertEqual(
            expectedMoney, originalMoney.divide(4)
        )
>>>>>>> 8b41058510cc343105eedc07d1466d8040fc1b19


if __name__ == "__main__":
    unittest.main()
