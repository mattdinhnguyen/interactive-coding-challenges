import unittest

from enum import Enum  # Python 2 users: Run pip install enum34
class Type(Enum):
    SELL = 0
    BUY = 1
class Transaction(object):
    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and \
            self.day == other.day and \
            self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' + \
            str(self.day) + ' price: ' + \
            str(self.price)
class StockTrader(object):

    def find_max_profit(self, prices, k):
        if None in (prices, k): raise TypeError("Params cant be None")
        if prices == [] or k <= 0: return []
        maxP, ans = 0, []
        for d in range(1, len(prices)):
            if prices[d] > prices[d-1]:
                maxP += prices[d]-prices[d-1]
                ans.extend([Transaction(Type.SELL, d, prices[d]),Transaction(Type.BUY, d-1, prices[d-1])])
        return maxP, ans
class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        stock_trader = StockTrader()
        self.assertRaises(TypeError, stock_trader.find_max_profit, None, None)
        self.assertEqual(stock_trader.find_max_profit(prices=[], k=0), [])
        prices = [5, 4, 3, 2, 1]
        k = 3
        self.assertEqual(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        self.assertEqual(profit, 10)
        self.assertTrue(Transaction(Type.SELL,
                                day=7,
                                price=3) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=6,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=4,
                                price=4) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=3,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=2,
                                price=7) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=0,
                                price=2) in transactions)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()
