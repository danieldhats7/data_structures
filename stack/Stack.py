class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack(object):
    def __init__(self, data=None):
        self.top = Node(data) if data is not None else None
        self.size = 0

    def __str__(self):
        s = "["
        node = self.top
        if node:
            while node:
                s += str(node)
                node = node.next
                if node:
                    s += ", "
        s += "]"
        return s

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return 'Any data on top'
        result = self.top.data
        self.top = self.top.next
        self.size -= 1
        return result

    def peek(self):
        if self.top is None:
            return 'Any data on top'
        return self.top.data

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
        # or simply:
        # return self.top is None
