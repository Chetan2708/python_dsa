class Node:
    def __init__(self,K):
        self.key= K
        self.next = None
class single:
    def __init__(self):
        self.head= None
    def printl(self):
        curr = self.head
        if self.head is None:
            print("EMPTY")
        else:
            while curr!=None :
                print(curr.key,end= "--->") 
                curr = curr.next
l = single()        
temp1 = Node(10)
l.head=temp1
temp2 = Node(20)
l.head.next=temp2
temp3 = Node(30)
l.head.next.next=temp3
l.printl()