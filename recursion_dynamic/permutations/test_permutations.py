import unittest
from collections import Counter
class Permutations(object):
    def find_permutations(self, string):
        if string in (None,""): return string
        perms = [""]
        for ch in string:
            perms = [s[:i] + ch + s[i:]
                 for s in perms
                 for i in range((s + ch).index(ch) + 1)] # cant replace with len,bc index return the first index of dup chars
        perms.sort()
        print(perms)
        return perms
    def find_permutations(self, string):
        if string in (None,""): return string
        perms = [""]
        for ch in string:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1): # all positions in perm to insert next ch in string
                    new_perms.append(perm[:i] + ch + perm[i:])   ###insert ch
                    if i<len(perm) and perm[i]==ch: break #handles duplication
            perms = new_perms
        perms.sort()
        print(perms)
        return perms
    def find_permutations(self, string):
        def btrack(path, counter):
            if len(path)==len(string):
                ans.append("".join(path))
            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    path += x # append char x to path list
                    counter[x] -= 1
                    btrack(path, counter) # recursively add char x to path
                    path.pop() # undo for next char in permutation: pop char x
                    counter[x] += 1 # revert x count
        if string in (None,""): return string
        ans = []
        btrack([], Counter(string)) # recursively add each char in string to empty path list till all in string added
        ans.sort()
        print(ans)
        return ans
    def find_permutations(self, string):
        res = []
        def backtrack(start, end):
            if start == end:
                res.append(string[:])
            for i in range(start, end):
                string[start], string[i] = string[i], string[start]
                backtrack(start+1, end)
                string[start], string[i] = string[i], string[start]
        backtrack(0, len(string))
        return res

class TestPermutations(unittest.TestCase):

    def test_permutations(self):
        permutations = Permutations()
        self.assertEqual(permutations.find_permutations(None), None)
        self.assertEqual(permutations.find_permutations(''), '')
        string = 'AABC'
        expected = [
            'AABC', 'AACB', 'ABAC', 'ABCA',
            'ACAB', 'ACBA', 'BAAC', 'BACA',
            'BCAA', 'CAAB', 'CABA', 'CBAA'
        ]
        self.assertEqual(permutations.find_permutations(string), expected)
        print('Success: test_permutations')


def main():
    test = TestPermutations()
    test.test_permutations()


if __name__ == '__main__':
    main()
