class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def insertatpos(head,n,pos):
    temp = Node(n)
    curr = head
    for i in range(1, pos-1):
        curr = curr.next 
        if curr is None:
            return head
    oldvar = curr.next    #storing the old value of current next 
    curr.next = temp
    temp.prev = curr
    temp.next = oldvar
    oldvar.prev = temp
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
n = int(input("Insert the value :"))
pos= int(input("Insert the position : "))
x=insertatpos(head,n,pos)
printlist(x)