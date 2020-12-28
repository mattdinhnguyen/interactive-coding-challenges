class Node(object):

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)
class MinHeap(object):
    def __init__(self, root=None):
        self.root = root
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))
    def create_level_lists(self):
        levelLists = [[self.root]]
        stax = levelLists[-1][:]
        while stax:
            stax = [c for n in stax for c in [n.left, n.right] if c]
            if stax: levelLists.append(stax)
        return levelLists
    def _insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            h = self.height(self.root)
            if h == 1:
                self.root.left = Node(data, self.root)
                return self.root.left
            elif h == 2 and self.root.right == None:
                self.root.right = Node(data, self.root)
                return self.root.right
            nextLastLevel, lastLevel = self.create_level_lists()[-2:]
            if len(lastLevel) == 2**(h-1): # full level, start a new level
                lastLevel[0].left = Node(data,lastLevel[0])
                return lastLevel[0].left
            else:
                for n in nextLastLevel:
                    if n.left == None:
                        n.left = Node(data, n)
                        return n.left
                    elif n.right == None:
                        n.right = Node(data, n)
                        return n.right
    def insert(self, data):
        n = self._insert(data)
        while n.parent and n.data < n.parent.data: # bubble up n.data
            n.parent.data, n.data = n.data, n.parent.data
            n = n.parent
        if n.left and n.left.data < n.data:
            n.left.data, n.data = n.data, n.left.data
            return n.left
        elif n.right and n.right.data < n.data:
            n.right.data, n.data = n.data, n.right.data
            return n.right
        else:
            return n
    def extract_min(self):
        if self.root == None: return None
        if self.root.left == self.root.right == None:
            n, self.root = self.root, None
            return n
        levelLists = self.create_level_lists()
        print(levelLists)
        lastNode = levelLists[-1][-1]
        lastNode.data, self.root.data = self.root.data, lastNode.data
        if lastNode.parent:
            if lastNode.parent.left == lastNode:
                lastNode.parent.left == lastNode.parent.right
            lastNode.parent.right = None
            return lastNode.data

    def peek_min(self):
        return self.root.data if self.root else None
import unittest
class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.peek_min(), None)
        self.assertEqual(heap.extract_min(), None)
        heap.insert(20)
        self.assertEqual(heap.peek_min(), 20)
        heap.insert(5)
        self.assertEqual(heap.peek_min(), 5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(5)
        self.assertEqual(heap.peek_min(), 5)
        heap.insert(3)
        self.assertEqual(heap.peek_min(), 3)
        self.assertEqual(heap.extract_min(), 3)
        self.assertEqual(heap.peek_min(), 5)
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()