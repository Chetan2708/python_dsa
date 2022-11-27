class Node:
    def __init__(self, k):
        self.key=k
        self.next = None 
def count(head):             #return the count of the list whose head is given 
    curr = head
    count = 0
    while curr:
        count += 1
        curr= curr.next

    return count
def get(head1, head2):
    length1 =count(head1)        #storing the count of the list1
    length2= count(head2)         #storing the count of the list2
    if length1 > length2:               
        d=length1-length2          #difference between length1 and length2 , calculate the bigger length and then subtarct
        return check(d, head1, head2)   # here length1 is the bigger so we return head1 as head1 so that we can use for loop to traverse till the difference
    else:
        d = length2 - length1       # here length2 is the bigger so we return head 2 as head 1 so that we can use for loop to traverse till the difference
        return check(d, head2, head1)
def check(d,head1, head2):    
    curr1 = head1
    curr2 = head2
    for i in range(d):
        if curr1 is None:
            return -1
        curr1=curr1.next
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1.key
        curr1=curr1.next
        curr2=curr2.next
common =Node(15)
head=Node(3)
head.next=Node(6)
head.next.next=Node(9)
head.next.next.next=common
head.next.next.next.next=Node(30)

head2= Node(9)
head2.next = common
head2.next.next=Node(30)
print(get(head, head2))
