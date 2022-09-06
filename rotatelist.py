

# def rot(l):             #list slicing
#     l2 = l[1:]+l[0:1]
#     return l2
    

# def rot(l):               #list methods
#     l.append(l.pop(0))
#     return l

def rot(l):                   #logic
    n = len(l)
    x = l[n-1]
    for i in range(n-1 , 0 , -1):
        l[i] = l [i-1]
    l[0]= x
    return l


l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(rot(l))