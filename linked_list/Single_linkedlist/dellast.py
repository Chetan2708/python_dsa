class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def dele(head):
    if head == None:
         return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:        
        curr= curr.next
    curr.next = None
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
head.next.next.next.next = Node(50)           # removing this by unlinking the previous node from it

head = dele(head)

printList(head)

