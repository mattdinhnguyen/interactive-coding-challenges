import unittest

class Sets(object):
    def find_power_set_backtrack(self, s):
        def dfs(s, path, ret):
            ret.append(path)
            for i in range(len(s)):
                dfs(s[i+1:], path+s[i], ret)

        ret = []
        dfs(s, '', ret)
        return ret
    def find_power_set_recursive(self, input_set):
        if input_set == '': return [input_set]
        def bfs(idx, ans):
            if idx < len(input_set):
                nans = []
                for a in ans:
                    if a+input_set[idx] not in ans:
                        nans.append(a+input_set[idx])
                return bfs(idx+1, ans+nans)
            return ans
        return bfs(0,[''])
    def find_power_set_iterative(self, input_set):
        output = ['']
        for ch in input_set:
            output += [s + ch for s in output if s+ch not in output]
        return output
class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        input_set = '123' # test data for dfs
        expected = ['','1','12','123','13','2','23','3']
        self.run_test(input_set, expected)
        input_set = ''
        expected = ['']
        self.run_test(input_set, expected)
        input_set = 'a'
        expected = ['', 'a']
        self.run_test(input_set, expected)
        input_set = 'ab'
        expected = ['', 'a', 'b', 'ab']
        self.run_test(input_set, expected)
        input_set = 'abc'
        expected = ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
        self.run_test(input_set, expected)
        input_set = 'aabc'
        expected = ['', 'a', 'aa', 'b', 'ab', 'aab', 'c', 'ac', 'aac', 'bc', 'abc', 'aabc']
        self.run_test(input_set, expected)
        print('Success: test_power_set')

    def run_test(self, input_set, expected):
        combinatoric = Sets()
        result = combinatoric.find_power_set_backtrack(input_set)
        self.assertEqual(result, expected)
        # result = combinatoric.find_power_set_recursive(input_set)
        # self.assertEqual(result, expected)
        # result = combinatoric.find_power_set_iterative(input_set)
        # self.assertEqual(result, expected)


def main():
    test = TestPowerSet()
    test.test_power_set()


if __name__ == '__main__':
    main()
