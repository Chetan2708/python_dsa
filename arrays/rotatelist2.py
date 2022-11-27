def rotate(l,d):                       #logic
    n1 = len(l)
    reverse(l,0,d-1)                  #reverse half before d
    reverse(l,d,n1-1)                 #reverse half after d 
    reverse(l,0,n1-1)                 #reverse full
    return l
def reverse(l,start , end):
    while start<end:
        l[start] ,l[end] = l[end],l[start]
        start = start + 1
        end= end - 1   

# def rotate(l,d):                      3list function
#     for i in range(0,d):
#         l.append(l.pop(0))
#     return l

# def rotate(l,d):                            #list slicing
#     l = l[d:]+l[0:d]
#     return l
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)  
d = int(input("the index from which to rotate"))
print(rotate(l,d))
