
# #already created ll


# class Node:
#     def __init__(self , k ):
#         self.key= k 
#         self.next = None
# def insert(head , x):
#         temp = Node(x)
#         temp.next = head
#         head = temp
#         return temp
# def display(head):
#         curr = head
#         while curr is not None:
#             print(curr.key , end = " --> ")
#             curr = curr.next
# temp1 = Node(10)
# head = temp1
# temp2 = Node(20)
# temp3 = Node(30)
# temp1.next = temp2
# temp2.next  = temp3
# x = int(input("enter the begining of the linked list of nodes:  "))
# z = insert(head , x)
# display(z)


# creating ll 


class Node:
    def __init__(self,K):
        self.key= K
        self.next = None
def ins(head,x):
    temp = Node(x)
    temp.next = head
    head = temp
    return head
head = None
head =ins(head, 10)
head =ins(head, 20)
head =ins(head, 30)

def display(head):
    curr = head
    while curr is not None:
         print(curr.key ,end =" -->")
         curr = curr.next

display(head)