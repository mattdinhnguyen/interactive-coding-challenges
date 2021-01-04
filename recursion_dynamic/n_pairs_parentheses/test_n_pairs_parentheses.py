import unittest

class Parentheses(object):
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
