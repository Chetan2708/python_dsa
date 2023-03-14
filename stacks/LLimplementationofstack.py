import math
class Node:
    def __init__(self,d):
        self.val=d
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.sz=0
    def push(self,val):
        valu = Node(val)
        valu.next = self.head
        self.head  = valu
        self.sz+=1
    def pop(self):
        if self.head==None:
            return math.inf
        res =  self.head.val
        self.head = self.head.next
        self.sz = self.sz-1
        return res
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end = "-->")
            curr = curr.next
a=stack()
a.push(0)
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.pop()
print(a.sz)
a.display() 

