class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def delPos(head,pos):
    if pos ==1:
       return head.next
    curr = head

    for i in range(1,pos-1):                          # loop over before 2 positions 
        curr = curr.next


    curr.next = curr.next.next        #deleting by unlinking 
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

head = delPos(head,4)

printList(head)
