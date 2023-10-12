import unittest
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
        self.assertEqual(
            expectedMoney, originalMoney.divide(4)
        )


if __name__ == "__main__":
    unittest.main()
