class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertPos(head, pos):
    if head is None:
        return
    first = head              # using 2 pointer approach like middle of linked list
    second = head 
    for i in range(pos):   #first pointer will move to the position given
        first = first.next
    if first == None:
        return second.next  
    while first.next != None:        #after first pointer will reach end, second pointer will reach the position asked from the back 
        second = second.next
        first = first.next
    second.next = second.next.next
    return head
def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
printList(head)
x= insertPos(head, 2)
printList(x)