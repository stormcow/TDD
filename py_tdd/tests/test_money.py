import unittest

from py_tdd.money import Money
from py_tdd.portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def testMultiplicationInEuros(self) -> None:
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self) -> None:
        originalMoney = Money(4002, "KRW")
        expectedMoney = Money(1000.5, "KRW")
        self.assertEqual(expectedMoney, originalMoney.divide(4))

    def testAddition(self) -> None:
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self) -> None:
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(expectedValue, actualValue)

    def testAdditionOfDollarsAndWons(self) -> None:
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portoflio = Portfolio()
        portoflio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portoflio.evaluate("KRW")
        self.assertEqual(expectedValue, actualValue)

    def testAdditionWithMultipleMissingExchangeRates(self) -> None:
        oneDollar = Money(1, "USD")
        oneEuro = Money(1, "EUR")
        oneWon = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, oneEuro, oneWon)
        with self.assertRaisesRegex(
            Exception,
            "Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]",
        ):
            portfolio.evaluate("Kalganid")


if __name__ == "__main__":
    unittest.main()
