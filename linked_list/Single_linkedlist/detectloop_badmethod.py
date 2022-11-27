class Node:
    def __init__(self, k):
        self.key=k
        self.next = None   
s= {} #using hashmap
flag = False
def check(head):
    global s,flag
    if head == None:
        flag = False
        return 
    if head not in s:
        s[head]= True
        flag = False
        check(head.next)
    else:
        flag =True
        return
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head.next.next.next.next = head
check(head)
if flag:
    print( "Loop found")
else:
    print("No Loop" )
