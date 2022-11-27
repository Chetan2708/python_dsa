class node:
    def __init__(self, k) :
        self.data = k 
        self.next = None
    
def rev(head):
    #Naive solution
    # stack = []             #linear time complexity but space complexity is high 
    # curr = head
    # while curr is not None:
    #     stack.append(curr.data)
    #     curr= curr.next
    # curr = head
    # while curr is not None:
    #     curr.data = stack.pop()
    #     curr = curr.next
    # return head
    ##Efficient solution
    prev = None
    curr = head 
    while curr:
        next = curr.next      # storing 20 in this next variable 
        curr.next = prev      # making none the next of 1st node as after reveresing it will be the end of the linked list
        prev = curr
        curr = next 
    return prev         # returning the last node as head , because curr and next now at the end of the linked list
def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end = " -->")
        curr = curr.next
    print()


head = node(10)
head.next= node(20)
head.next.next= node(30)
head.next.next.next= node(40)
head.next.next.next.next =node(50)
printlist(head)
x= rev(head)
printlist(x)