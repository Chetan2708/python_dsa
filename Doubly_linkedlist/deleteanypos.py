class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def delatpos(head,pos):
    count  = 0
    curr = head
    while curr:          #edge case 
        count+=1
        curr = curr.next
    if pos > count:        
        return 
    curr = head
    for i in range(1, pos): 
        curr = curr.next  
        if curr is None:
            return head
    curr.prev.next = curr.next         #change link of prev , of current to next of current , thus removing curr
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
pos= int(input("Insert the position : "))
x=delatpos(head,pos)
printlist(x)
