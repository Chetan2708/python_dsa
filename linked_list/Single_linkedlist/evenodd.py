class Node:
    def __init__(self, k):
        self.key=k
        self.next = None 
def evnod(head):
    es , ee , os , od = None, None, None , None 
    curr = head
    while curr != None:
        z = curr.key
        if  z% 2 == 0:
            if es ==None:
                es  = curr
                ee = es
                curr = curr.next
            else:
                ee.next = curr
                ee = ee.next #updating even end
                curr = curr.next
        else:
            if os==None:
                os  = curr
                oe = os
                curr = curr.next
            else:
                oe.next = curr
                oe = oe.next #updating odd end
                curr = curr.next
    if es == None or os==None:
        return head
    ee.next = os 
    oe.next = None
    return es 
def printl(head): 
    curr = head
    while curr != None:
        print(curr.key , end = "-->")
        curr = curr.next

head= Node(17)
head.next= Node(15)
head.next.next= Node(8)
head.next.next.next= Node(12)
head.next.next.next.next= Node(10)
head.next.next.next.next.next= Node(5)
head.next.next.next.next.next.next=Node(4)

x = evnod(head)
printl(x)
