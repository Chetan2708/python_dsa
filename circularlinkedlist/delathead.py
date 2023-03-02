class Node:
    def __init__(self, k):
        self.data = k 
        self.next = None

def insert(head):
    curr = head
    # while curr.next!= head:           #naive solution
    #     curr = curr.next        
    # curr.next = head.next
    # return curr.next

    head.data = head.next.data      #swapping both data's of head next and head itself
    head.next = head.next.next
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
head=insert(head)
print1(head)