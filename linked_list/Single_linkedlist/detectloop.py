#Floyd cycle detection

class Node:
    def __init__(self, k):
        self.key=k
        self.next = None 
def check(head):
    fast ,slow= head , head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow== fast:
            return slow
def remove(head):
    slow = check(head)
    start = head
    while start.next != slow.next:
        slow = slow.next
        start = start.next
    slow.next = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head
remove(head)
