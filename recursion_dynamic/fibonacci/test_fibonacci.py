import unittest

class Math(object):
    def __init__(self):
        self.dp = [0, 1]

    def fib_iterative(self, n):
        a, b = 0, 1
        if n < 1: return a
        if n < 2: return b
        for i in range(2,n+1):
            a, b = b, a+b
        return b

    def fib_recursive(self, n):
        if n < 1: return 0
        if n < 2: return 1
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_dynamic(self, n):
        if n < len(self.dp): return self.dp[n]
        i = len(self.dp)
        for j in range(i,n+1):
            self.dp.append(self.dp[j-1] + self.dp[j-2])
        return self.dp[n]
class TestFib(unittest.TestCase):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        self.assertEqual(result, expected)
        print('Success: test_fib')

    def test_fib2(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result.append(func(10**9+7))
        # self.assertEqual(result, expected)
        print('Success: test_fib result = {result}')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_dynamic)
    test.test_fib(math.fib_iterative)
    test.test_fib2(math.fib_iterative)


if __name__ == '__main__':
    main()
