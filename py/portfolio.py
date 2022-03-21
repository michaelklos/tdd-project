from money import Money

import functools
import operator


class Portfolio:
    def __init__(self) -> None:
        self.moneys = []
        self._eur_to_usd = 1.2

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            return aMoney.amount * self._eur_to_usd

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys), 0
        )
        return Money(amount=total, currency=currency)
