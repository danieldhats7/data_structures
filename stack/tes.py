from Stack import *

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n4.next = n5
n3.next = n4
n2.next = n3
n1.next = n2

def reverseList(head):
        
    head = head
    prev = head.next
    def rec(head, prev):
        if head is None:
            return prev
        next = head.next
        head.next = prev
        return rec(next, head)
        
    return rec(head, prev)

r = reverseList(n1)


