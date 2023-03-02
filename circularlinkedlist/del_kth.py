class Node:
    def __init__(self, k):
        self.data = k 
        self.next = None

def deleete(head, k):
    curr= head
    if head.next == head :
        return 0
    elif k ==1:
        head.data = head.next.data
        head.next = head.next.next
        return head
    curr = head
    for i in range(1, k-1):          #2 pos less because curr will increment eachtime loop will run 
        curr = curr.next
    curr.next = curr.next.next       #changing link
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
# head.next = head
k = int(input( ))
head=deleete(head,k)
if head==0 :
    print("EMPTIED or invalid input")
else:
    print1(head)