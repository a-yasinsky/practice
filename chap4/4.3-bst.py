class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, arr = None):
        arr = arr or []
        if len(arr)  > 0:
            self.root = self.builtBST(arr)

    def print_tree(self):
        return self.preorder_print(self.root, [], 0)

    def preorder_print(self, start, tree, level):
        if start:
            if(len(tree) <= level):
                tree.insert(level,[])
            tree[level].append(start.value)
            self.preorder_print(start.left, tree,  level + 1)
            self.preorder_print(start.right, tree,  level + 1)
        return tree

    def builtBST(self, arr):
        length = len(arr)
        if length == 1:
            return Node(arr[0])
        middle = length // 2
        node = Node(arr[middle])
        node.left = self.builtBST(arr[0:middle])
        if middle + 1 < length:
            node.right = self.builtBST(arr[middle+1:])
        else:
            node.right = None
        return node

bt = BinaryTree([1,2,3,4,5])
print(bt.print_tree())
