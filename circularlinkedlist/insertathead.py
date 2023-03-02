class Node:
    def __init__(self, k):
        self.data = k 
        self.next = None

def insert(head, n):
    temp = Node(n)
    curr = head
    # while curr.next!= head:           #naive solution
    #     curr = curr.next        
    # curr.next = temp
    # temp.next = head
    # return temp
                                          
                                      #efficient solution
    temp.next = head.next       #inserting temp just after head
    head.next = temp
    t = head.data      
    head.data= temp.data         #swapping head.next and head  
    temp.data = t
    return head 
def print1(head):
    if head == None:
        return None
    curr = head
    print(curr.data, end="-->")
    curr=curr.next
    while curr!=head:
        print(curr.data, end ="-->")
        curr = curr.next
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head
n = int(input())
head=insert(head, n)
print1(head)