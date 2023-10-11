import unittest
from dataclasses import dataclass


@dataclass
class Dollar:
    amount: int

    def times(self, multipllier: int) -> "Dollar":
        return Dollar(self.amount * multipllier)


class TestMoney(unittest.TestCase):
    def testMultiplication(self) -> None:
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)


if __name__ == "__main__":
    unittest.main()
