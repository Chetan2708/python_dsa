class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def dele(head):
    if head == None:
         return None
    else:
        return head.next                  #accessing head.next

def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()


head = Node(10)             # removing this by directly accessing head.next 
head.next = Node(20)     
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)

head = dele(head)

printList(head)

