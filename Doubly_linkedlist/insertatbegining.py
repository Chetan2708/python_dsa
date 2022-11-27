class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        self.prev = None
def insertathead(head,n):
    temp4 = Node(n)
    temp4.next = head     #if head is null , temp ka next null ho jayga no problem in  that
    if head != None:      
        head.prev = temp4           #if head is null , it is not possible to access the previous of null so saving it in as an edge case
    head = temp4                 
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
n = int(input())
x=insertathead(head,n)
printlist(x)