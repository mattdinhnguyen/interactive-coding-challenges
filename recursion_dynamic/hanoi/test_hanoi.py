import unittest
from stacks_queues.stack.stack import Stack
class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        if None in (src,dest,buff): raise TypeError("Stack params cant be None")
        def _move_disks(num_disks, src, dest, buff):
            if num_disks:
                self.move_disks(num_disks-1, src, buff, dest) # move all, except bottom disk to buff, using dest as buff
                dest.push(src.pop()) # move bottom disk to dest
                self.move_disks(num_disks-1, buff, dest, src) # move rest from buff to dest, using src as buff
        _move_disks(num_disks, src, dest, buff)
class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        hanoi = Hanoi()
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        self.assertRaises(TypeError, hanoi.move_disks, num_disks, None, None, None)

        print('Test: 0 disks')
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi.move_disks(num_disks, src, dest, buff)
        self.assertEqual(dest.pop(), 5)

        print('Test: 2 or more disks')
        for disk_index in range(num_disks, -1, -1):
            src.push(disk_index)
        hanoi.move_disks(num_disks, src, dest, buff)
        for disk_index in range(0, num_disks):
            self.assertEqual(dest.pop(), disk_index)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()
