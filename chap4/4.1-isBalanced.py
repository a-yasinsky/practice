class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

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

    def isBalanced(self):
        if not self.root:
            return True
        if(abs(self.deepth(self.root.left) - self.deepth(self.root.right) <= 1)):
            return True
        else:
            return False

    def deepth(self, node):
        if(not node):
            return 0
        return max(
                self.deepth(node.left),
                self.deepth(node.right)
                ) + 1

bt = BinaryTree('a')
bt.root.left = Node('b')
bt.root.right = Node('c')
bt.root.left.left = Node('b-l')
bt.root.left.right = Node('b-r')
#bt.root.left.right.right = Node('b-r-r')
print(bt.print_tree())
print(bt.isBalanced())
