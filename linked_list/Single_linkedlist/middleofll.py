class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def mid(head):
    if head == None:
        return 
    slow= head                             #efficient implementation without looping slow and fast pointer when fast reaches end point , slow will give mid
    fast=head
    while fast!= None and fast.next!=None:          #if u wanty the slow pointer to be at 1 position before the middle point , 
        #prev = slow
        slow = slow.next                             #store slow in a variable prev , prev = slow
        fast = fast.next.next
    #prev.next = prev.next.next                      u can remove the middle pointer
    return slow.key    
head = Node(10)             
head.next = Node(20)     
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
 # the fast pointer moves with double the speed of the slow pointer, 
 # that's why when the fast pointer reaches the end of the linked list, the slow pointer is in the middle. 
 # That's the reason why the fast pointer moves fast.next.next. This means that fast skips one and jumps 2 fields in each iteration, 
 # while the slow pointer only moves one. That's also the reason you check fast and fast.next in the while loop condition,
 #  to make sure the next pointer is not None, because you want to call next on it.

    # count = 0                                # Naive implementaion
    # curr = head
    # while curr :
    #     curr = curr.next
    #     count+=1
    
    # curr = head
    # for i in range (count//2):
    #     curr = curr.next
    # return curr.key
x = mid(head)

print(x)

