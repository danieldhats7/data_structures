class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self, root=None):
        self.root = Node(root)

    def print(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            self.print(node.left)
        self.s += str(node) + " "
        if node.right is not None:
            self.print(node.right)
        
    def __str__(self):
        self.s = ""
        self.print()
        return self.s

    def insert(self, newNode, node=None):
        if node is None:
            node = self.root
        if newNode.data < node.data:
            if node.left is None:
                node.left = newNode
            else:
                self.insert(newNode, node.left)
        elif newNode.data > node.data:
            if node.right is None:
                node.right = newNode
            else:
                self.insert(newNode, node.right)

    def find(self, data, node=None):
        if node is None:
            node = self.root
        if data < node.data:
            if node.left is None:
                return 'Not Found'
            return self.find(data, node.left)
        elif data > node.data:
            if node.right is None:
                return 'Not Found'
            return self.find(data, node.right)
        else:
            return 'Found!!'

    def maxdepth(self, node=None):
        if node is None:
            node = self.root
        depth = 0
        level = [node] if node else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth
