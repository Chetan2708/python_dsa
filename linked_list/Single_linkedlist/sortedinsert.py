class node:
    def __init__(self , k):
        self.data = k
        self.next = None

def ins(head , x):
    temp = node(x)
    if head ==None:
        return temp
    elif x < head.data:
        temp.next = head
        return temp
    else:
        curr = head
        while curr.next!= None and curr.next.data < x:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head

def print1(head):
    curr = head
    while curr!=None:
        print(curr.data , end = " --> ")
        curr = curr.next
    print()
head = node(10)
head.next = node(20)
print1(head)
head= ins(head, 15)
print1(head)