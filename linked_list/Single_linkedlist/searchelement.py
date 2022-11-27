class Node():
    def __init__(self,K):
        self.key= K
        self.next = None

def search(head,x):
    curr = head
    pos=1
    while curr!=None :
        if curr.key==x :
            return pos
        pos = pos+1
        curr = curr.next
    return -1
        
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
head =  temp1
x= int(input())
print(search(head,x))



