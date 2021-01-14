import unittest
class Bits:
    def __init__(self):
        self.MAX_BITS = 32

    def flip_bit(self, num):
        if num == None: raise TypeError("Cant be None")
        if num == 0: return 1
        if num == -1: return self.MAX_BITS
        while num and num & 1 == 0:
            num >>= 1
        oneMax = cur2Max = cur1Max = 0
        while num and num & 1 == 1:
            cur1Max += 1
            num >>= 1
            if num & 0b11 == 2:
                if cur2Max:
                    oneMax = max(oneMax, cur2Max+cur1Max)
                if num:
                    num >>= 1
                    cur2Max, cur1Max = cur1Max+1, 0
            elif num & 0b11 == 0:
                oneMax = max(oneMax, cur2Max+cur1Max)
                cur2Max = cur1Max = 0
                while num and num & 1 == 0: num >>= 1
        return oneMax
class TestBits(unittest.TestCase):

    def test_flip_bit(self):
        bits = Bits()
        self.assertRaises(TypeError, bits.flip_bit, None)
        self.assertEqual(bits.flip_bit(0), 1)
        self.assertEqual(bits.flip_bit(-1), bits.MAX_BITS)
        num = int('00001111110111011110001111110000', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00000100111011101111100011111011', base=2)
        expected = 9
        self.assertEqual(bits.flip_bit(num), expected)
        num = int('00010011101110111110001111101111', base=2)
        expected = 10
        self.assertEqual(bits.flip_bit(num), expected)
        print('Success: test_print_binary')


def main():
    test = TestBits()
    test.test_flip_bit()


if __name__ == '__main__':
    main()
