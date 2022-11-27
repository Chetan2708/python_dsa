class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def delathead(head):
    if head is None:
        return
    if head.next is None:
        #del head         #no need to delete the node using del keyword explicitly as python has automatic garbage collection that deallocates the memory
        return None        
    head = head.next
    head.prev= None
    return head
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
x=delathead(head)
printlist(x)