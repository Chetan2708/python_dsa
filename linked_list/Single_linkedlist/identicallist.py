#GFG question

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def ident(head,head2):
    while head != None and head2 != None:
        if head.key !=head2.key:
            return False
        head= head.next 
        head2 = head2.next
    if head != None or head2 != None:
        return False
    else:
        return True

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)
head2.next.next.next = Node(40)
head2.next.next.next.next = Node(50)
x = ident(head, head2)
print(x)