class Node:
    def __init__(self, k):
        self.data = k 
        self.next = None

def rem(head):
    curr = head
    while curr != None  and curr.next !=None:   #if single node linked list then curr.next should be None 
        if curr.data == curr.next.data:         # , SO it will check for NONE.NEXT.DATA in the next iteration which is illegal
                curr.next = curr.next.next
        else:    
            curr = curr.next
def print1(head):
    curr = head
    while curr!=None:
        print(curr.data , end = " --> ")
        curr = curr.next
    print()
head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
rem(head)
print1(head)