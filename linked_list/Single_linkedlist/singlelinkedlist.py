class Node():
    def __init__(self,K):
        self.key= K
        self.next = None


def printlist(head):
    curr = head
    while curr!= None:
        print(curr.key , end = " -- >")
        curr = curr.next

temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
head =  temp1  #directly assigning it to the first element , 
#not thinking of the empty linked list here (for empty linked list create another class and print )
head.next = temp2
temp2.next = temp3
printlist(head)


#short implementation of linked list
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# print(head.key , head.next.key , head.next.next.key ) 
