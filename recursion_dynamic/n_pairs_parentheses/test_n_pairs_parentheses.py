import unittest

class Parentheses(object):
    # https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution
    def find_pair(self, num_pairs):
        if num_pairs == None: raise TypeError("Param cant be None")
        if num_pairs < 0: raise ValueError("Param cant be negative or 0")
        if num_pairs == 0: return []
        ans = []
        def backtrack(string, open, close):
            if len(string) == 2*num_pairs:
                ans.append(string)
                return
            if open < num_pairs:
                backtrack(string+"(", open+1, close) # adding all open paren
            if close < open:
                backtrack(string+")", open, close+1) # adding matching close paren
        backtrack("", 0, 0)
        return ans
    def find_pair(self, n):
        if n == None: raise TypeError("Param cant be None")
        if n < 0: raise ValueError("Param cant be negative or 0")
        if n == 0: return []
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(1,n + 1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        dp[i] += ['(' + x + ')' + y]
        dp[n].sort()
        return dp[n]
    # https://leetcode.com/problems/generate-parentheses/discuss/10283/Python-simple-stack-solution-without-recursion
    # variable l is current left parenthesis count
    # variable r is current right parenthesis count
    # l - r < 0 means this is not a valid parenthesis
    def find_pair0(self, n):
        if n == None: raise TypeError("Param cant be None")
        if n < 0: raise ValueError("Param cant be negative or 0")
        if n == 0: return []
        res = []
        s = [("(", 1, 0)] # stack s of (string,l,r)
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n: continue # invalid, stop stack append, keep om poppinng stack till empty
            if l == n and r == n: res.append(x) # has n pairs
            s.append((x+"(", l+1, r)) # build strings of left parens till l == n
            s.append((x+")", l, r+1)) # add right parens till l == r == n
        res.sort()
        return res
class TestPairParentheses(unittest.TestCase):

    def test_pair_parentheses(self):
        parentheses = Parentheses()
        self.assertRaises(TypeError, parentheses.find_pair, None)
        self.assertRaises(ValueError, parentheses.find_pair, -1)
        self.assertEqual(parentheses.find_pair(0), [])
        self.assertEqual(parentheses.find_pair(1), ['()'])
        self.assertEqual(parentheses.find_pair(2), ['(())',
                                                '()()'])
        self.assertEqual(parentheses.find_pair(3), ['((()))',
                                                '(()())',
                                                '(())()',
                                                '()(())',
                                                '()()()'])
        print('Success: test_pair_parentheses')


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == '__main__':
    main()
