from unittest import result


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right - right

class TreeNode:
    resul = None
    def __init__(self, lis=None):
        if lis:
            resul = Node()
            actual_node = resul
            way = 'l'
            for i in lis:
                if i:
                    actual_node.val = i
                    actual_node.left = Node()
                    actual_node.right = Node()
                    acutal_node = actual_node.left
                else:    
                    way = 'r'



                Node(val=i)