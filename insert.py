
def ins(l , pos , x ,n):
    for i in range(n-1, pos-2 , -1):
        l[i+1] = l[i] 
    l[pos] = x
    return l


l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
pos = int(input("enter the position of the observation"))
x = int(input("enter the x "))
l.append(None)
print(ins(l , pos , x ,n ))