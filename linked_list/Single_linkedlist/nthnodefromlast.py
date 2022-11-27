class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


def insertPos(head, pos):
    if head is None:
        return
    # curr = head                         # using length of linked list
    # len = 0
    # while curr:
    #     curr = curr.next
    #     len += 1
    # if len < pos:
    #     return
    # curr = head
    # for i in range(1, len-pos+1):         #relation of length and position
    #     curr = curr.next
    # print(curr.key)
    
    first = head              # using 2 pointer approach like middle of linked list
    second = head 
    for i in range(1,pos):   #first pointer will move to the position given
        if first == None:
            return
        first = first.next
    while first.next!= None:        #after first pointer will reach end, second pointer will reach the position asked from the back 
        second = second.next
        first = first.next
    print(second.key)

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
insertPos(head, 2)
