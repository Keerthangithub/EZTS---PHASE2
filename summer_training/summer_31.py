class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def _init_(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

# Example usage
t1 = Tree()
t1.root = t1.create(t1.root, 10)
t1.root = t1.create(t1.root, 5)
t1.root = t1.create(t1.root, 20)
t1.root = t1.create(t1.root, 7)

# Traversals
print("Inorder traversal:")
t1.inorder(t1.root)

print("Preorder traversal:")
t1.preorder(t1.root)

print("Postorder traversal:")
t1.postorder(t1.root)