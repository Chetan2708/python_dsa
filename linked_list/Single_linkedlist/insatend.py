class node:
    def __init__(self, k) :
        self.key = k
        self.next = None
class LL:
    def head(self):
        self.head = None
    def ins(self , head , x):
        temp = node(x)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next =  temp
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.key , end = "-->")
            curr = curr.next
l = LL()
n1= node(10)
l.head = n1
n2  = node(20)
n1.next = n2
n3 = node(30)
n2.next = n3
l.ins(l.head , 15)
l.display()



# class node:
#     def __init__(self , k):
#         self.key = k
#         self.next = None
# def ins(head, x):                                                                                      
#     if head == None:
#         return node(x)
#     curr = head
#     while curr.next is not None:
#         curr = curr.next
#     curr.next = node(x)
#     return head

# head = None
# head =ins(head , 10)
# head =ins(head , 20)
# head =ins(head , 30)
# head =ins(head , 40)
# def print_list(head):
#     curr =head
#     while curr is not None:
#         print(curr.key ,  end = " --> ")
#         curr = curr.next
# print_list(head)
