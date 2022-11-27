class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def rev(head):
        curr = head
        prev= None
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        return prev.prev
def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end="-->")
        curr= curr.next
head = Node(10)
temp1 = Node(20)
temp2= Node(30)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = None
x=rev(head)
printlist(x)