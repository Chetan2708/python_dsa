class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def delattail(head):
    if head == None:
         return None
    if head.next == None:
        return None
    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    return head
def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end="-->")
        curr= curr.next
head = Node(10)
temp1 = Node(20)
temp2= Node(30)
temp3= Node(30)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1
temp2.next = temp3
temp3.prev=temp2
temp3.next = None
x=delattail(head)
printlist(x)