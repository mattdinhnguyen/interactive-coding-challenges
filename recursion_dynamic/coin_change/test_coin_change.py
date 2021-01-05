import unittest

class CoinChanger(object):

    def make_change(self, coins, amount): # DP Time Complexity: O(n^m), n = len(coins), m = amount / min(coins)
        def helper(total: int, start: int) -> int:
            if total > amount: return 0
            elif total == amount: return 1
            result = 0
            for i in range(start, len(coins)): # traverse the coins tree for each coin value, starting at coins[0]
                result += helper(total + coins[i], i)
            return result
        if not amount: return 0
        return helper(0, 0)
    def make_change(self, coins, amount): # DP Time Complexity: O(n*m), n = len(coins), m = amount
        if not amount: return 0
        dp = [1] + [0] * amount # dp[0..amount] = # of ways for various amounts
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin] # dp[coin] = 0+dp[0]
        return dp[amount]
class Challenge(unittest.TestCase):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        self.assertEqual(coin_changer.make_change([1, 2], 0), 0)
        self.assertEqual(coin_changer.make_change([1, 2, 3], 5), 5)
        self.assertEqual(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()
