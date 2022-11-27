#important question  leet code 237 
class node: 
    def __init__(self ,k):
        self.data = k
        self.next = None

def delete(ptr):
    temp = ptr.next       #copying the next node to the temp
    ptr.data = temp.data  #copying the new data to pointer 
    ptr.next = temp.next

def print1(head):
    curr = head
    while curr!=None:
        print(curr.data , end = " --> ")
        curr = curr.next
    print()

head = node(10)
head.next = node(10)  #deleting
head.next.next = node(20)
head.next.next.next = node(30)

print1(head)
delete(head.next)
print1(head)

